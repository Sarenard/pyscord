import requests
import websocket
import json
import threading
import time
import global_vars

def send_json_request(ws, request):
        ws.send(json.dumps(request))

def recieve_json_response(ws):
        response = ws.recv()
        if response:
                return json.loads(response)

def heartbeat(interval, ws):
        print('Heartbeat begin')
        time.sleep(0.5)
        while True:
            heartbeat_send(ws)
            time.sleep(interval)
            
def heartbeat_send(ws):
    heartbeatJSON = {
            "op": 1,
            "d": "null"
    }
    send_json_request(ws, heartbeatJSON)
    global_vars.heartbeat_sent_time = time.time()

headers = {
        "Authorization": f"Bot {global_vars.token}"
}
r2 = requests.get(global_vars.gateway_url, headers=headers) 

ws = websocket.WebSocket()

def connect(ws,wss_url,gateway_ver):
    ws.connect(f'{wss_url}/?v={gateway_ver}&encoding=json')

    event = recieve_json_response(ws)
    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    print("Heartbeat time interval: ",heartbeat_interval)

    thread = threading.Thread(target= heartbeat, args=(heartbeat_interval,ws))
    thread.start()

    return event

def identify(ws):
    payload = {
        "op": 2,
        "d": {
            "token": global_vars.token,
            "intents": 32767,
            "properties": {
                "$os": "linux",
                "$browser": "chrome",
                "$device": "pc"
            }
        }
    }
    send_json_request(ws,payload)

    event = recieve_json_response(ws)
    if (event != None): print("Bot is ready af") 
    return event


def listener(ws):
    while True:
        event = recieve_json_response(ws)
        print(event)
        if event != None:

            global_vars.response_recieve_time = time.time()
        
            if event["op"] == 0:                                                                                 #* Dispatch
                s = event["s"]
                
                if event["t"] == "INTERACTION_CREATE" and event["d"]["type"] == 2:                                         #* Commands
                    print(event["d"]["data"]["name"] + " command used.")
                
                    try:
                        name = event["d"]["data"]["name"]
                        name = "_".join(name.split())
                        globals()[name](ws,event)
                    except Exception as e:
                        print(e)

                elif event["t"] == "INTERACTION_CREATE" and event["d"]["type"] == 3:                                         #* Message Components
                    print(event["d"]["data"]["custom_id"] + " interaction used.")

                    try:
                        globals()[event["d"]["data"]["custom_id"]](ws,event)
                    except Exception as e:
                        print(e)
                elif event["t"] == "VOICE_STATE_UPDATE":
                    global_vars.voice_session_id = event["d"]["session_id"]
                elif event["t"]== "VOICE_SERVER_UPDATE":
                    global_vars.vs_info = event["d"]



            elif event["op"] == 11:                                                                             #* Heartbeat ACK
                print("Heartbeat Recieved")
                global_vars.latency = round((time.time() - global_vars.heartbeat_sent_time)*1000)

            elif event["op"]== 7:                                                                                 #* Reconnect
                resume(ws)

            else:
                print(event)

if __name__ == "__main__":
    Hello_event= connect(ws,r2.json()["url"],global_vars.gateway_ver)
    Ready_event = identify(ws)

    global_vars.bot_session_id = Ready_event["d"]["session_id"]

    thread2 = threading.Thread(target= listener, args=(ws,))
    thread2.start()


def resume(ws):
    payload = {
    "op": 6,
    "d": {
        "token": globals.token,
        "session_id": global_vars.bot_session_id,
        "seq": global_vars.s
        }
    }
    send_json_request(ws,payload)

    event = recieve_json_response(ws)
    if event["op"] == 9:
        print("Connection died. Attempting re-identify")
        identify(ws)
    else:
        print(event)
    return event