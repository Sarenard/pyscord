import important
import pyscord

bot = pyscord.Client(token=important.token, id=877568674666524682, api_version=9)

@pyscord.listener.event_on_ready
async def on_ready():
    print("Le bot est pret")

@pyscord.listener.event_message
async def on_message(message):
    print(message.content)
        
bot.run()