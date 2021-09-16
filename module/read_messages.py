from datetime import *
import important
import pyscord

bot = pyscord.Client(token=important.token)

@pyscord.listener.event_on_ready
async def on_ready():
    print("démarrage du read_messages")

@pyscord.listener.event_message
async def on_message(message):
    print(datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S.%f ') + bot.getguild(message.guild_id).name + " | " + bot.getchannel(message.channel_id).name + " | " + message.author.name + " > ", end = "")
    print(message.content)

bot.run()