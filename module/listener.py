import threading
import websocket
import requests
import messages
import asyncio
import json
import time

global func
func=None
def event_message(function_to_decorate=None, event=None):
    global func
    if event == {} : return
    if func != None: asyncio.run(func(messages.Message(event['d'], api_version=api_version, basic_header=basic_header)))
    if function_to_decorate != None:
        func = function_to_decorate
        try:
            asyncio.run(func(messages.Message(event['d'], api_version=api_version, basic_header=basic_header)))
        except:
            pass

global func2
func2 = None
def event_on_ready(function_to_decorate=None):
    global func2
    if function_to_decorate != None:
        func2 = function_to_decorate
        try:
            asyncio.run(func2())
        except:
            pass

class Listener:
    def __init__(self, token, basic_head=None, api_ver=9):
        global basic_header, api_version
        basic_header = basic_head
        api_version = api_ver
        self.token = token

    def send_json_request(ws, request):
        ws.send(json.dumps(request))

    def recieve_json_response(ws):
        response = ws.recv()
        if response: return json.loads(response)

    def heartbeat(interval, ws):
        time.sleep(0.5)
        while True:
            Listener.send_json_request(ws, { "op": 1, "d": "null" })
            time.sleep(interval)

    def connect(ws,wss_url):
        ws.connect(f'{wss_url}/?v=9&encoding=json')
        event = Listener.recieve_json_response(ws)
        heartbeat_interval = event['d']['heartbeat_interval'] / 1000
        threading.Thread(target=Listener.heartbeat, args=(heartbeat_interval,ws)).start()
        return event

    def identify(self,ws):
        #TODO : implementer indents dans Client() (client.py)
        Listener.send_json_request(ws,{"op": 2, "d": {"token": self.token, "intents": 32767, "properties": { "$os": "windows", "$browser": "chrome", "$device": "pc"}}})
        event = Listener.recieve_json_response(ws)
        if (event != None): event_on_ready()
        return event

    def listener(ws):
        while True:
            event = Listener.recieve_json_response(ws)
            if event == None : return
            if event["t"] == "MESSAGE_CREATE" : event_message(event=event)
            if event["op"]== 7: reconnection(ws)

    def reconnection(ws):
        payload = { "op": 6, "d": {"token": globals.token, "session_id": global_vars.bot_session_id, "seq": global_vars.s}}
        send_json_request(ws,payload)
        event = recieve_json_response(ws)
        if event["op"] == 9:
            print("Perte de connection, tentative de reconnection")
            identify(ws)

    def start(self):
        global ws
        ws = websocket.WebSocket()
        Listener.connect(ws,"wss://gateway.discord.gg")
        self.identify(ws)
        threading.Thread(target=Listener.listener, args=(ws,)).start()

    def stop(self):
        global ws
        ws.close()