import important
import pyscord

bot = pyscord.Client(token=important.token)

@pyscord.listener.event_on_ready
async def on_ready():
    print("Le bot est pret")

@pyscord.listener.event_message
async def on_message(message):
    if message.content.startswith("&"):
        bot.reply(message, "le bot est off pour le moment, il est remplacé par ce message jusqu'a son rétablissement (si le bot normal marche merci de ping <@652889258343792661>)")
        
bot.run()