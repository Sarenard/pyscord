import pyscord

import discord
import requests
import random

bot = pyscord.Client(token="ODc3NTY4Njc0NjY2NTI0Njgy.YR0hhA.qahcocZ66Ic7dQk8mgXLvwt4kK8")
print(bot.getchannel(826074242789408849).sendmessage("test").author.id)

