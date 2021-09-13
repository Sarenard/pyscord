import pyscord
import discord
import requests
import random

bot = pyscord.Client(token="ODc3NTY4Njc0NjY2NTI0Njgy.YR0hhA.qahcocZ66Ic7dQk8mgXLvwt4kK8", api_version=9)

@pyscord.listener.event_message
def on_message(message):
    print(message.content)
    print(message.author.id)

print(bot.getchannel(881177511629832243).sendmessage("test").author.id)
bot.run()