import asyncio
import websockets
import random
import threading
import json
import time

async def hello():
    global websocket
    async with websockets.connect("wss://gateway.discord.gg/?v=9&encoding=json") as websocket:
        await on_message(await websocket.recv())

async def on_message(msg):
    global websocket
    print(msg)
    msg = json.loads(msg)
    if msg["op"] == 10 :
        async def t(msg):
            global websocket
            heartbeat_interval = msg["d"]["heartbeat_interval"]
            time.sleep(heartbeat_interval * random.random()/1000)
            while True:
                await websocket.send({"op": 1,
                                      "d": 251 })
                time.sleep(heartbeat_interval/1000)
        threading.Thread(target=asyncio.run, args=(t(msg),)).start()
        

asyncio.run(hello())

