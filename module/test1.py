import pyscord
import random
import discord

bot = pyscord.Client(token="ODc3NTY4Njc0NjY2NTI0Njgy.YR0hhA.qahcocZ66Ic7dQk8mgXLvwt4kK8", api_version=9)
liste = bot.getguilds()
print(liste.getnames())
print(liste.getids())