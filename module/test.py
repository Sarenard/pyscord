import important
import pyscord

bot = pyscord.Client(token=important.token)

@pyscord.listener.event_on_ready
async def on_ready():
    print("Le bot est pret")

@pyscord.listener.event_message
async def on_message(message):
    if message.content.startswith("/print"):
        bot.reply(message, message.content.replace("/print", ""))
    if message.mention_everyone:
        bot.reply(message, "merci de ne pas ping everyone!")
        
bot.run()