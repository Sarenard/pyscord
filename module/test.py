import important
import pyscord

bot = pyscord.Client(token=important.token)

@pyscord.listener.event_on_ready
async def on_ready():
    print("Le bot est pret")

@pyscord.listener.event_message
async def on_message(message):
    print(message.content)
        
bot.run()