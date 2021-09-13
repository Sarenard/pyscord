import pyscord
import threading

bot = pyscord.Client(token="ODc3NTY4Njc0NjY2NTI0Njgy.YR0hhA.qahcocZ66Ic7dQk8mgXLvwt4kK8", api_version=9)

@pyscord.listener.event_message
def on_message(message):
    if message.content == "ping":
        bot.sendmessage(message.channel_id, "pong")
        
@pyscord.listener.event_on_ready
def on_ready():
    print("Le bot est pret")

bot.run()