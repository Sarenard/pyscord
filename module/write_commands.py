import important
import channels
import pyscord

bot = pyscord.Client(token=important.token)

def change_serveur():
    global data
    liste_servs = [str(guild.name) for guild in [bot.getguild(id) for id in bot.getguilds().getids()]]
    liste_servs_ids = [str(guild.id) for guild in [bot.getguild(id) for id in bot.getguilds().getids()]]
    print(liste_servs_ids)
    for x in range(len(liste_servs)):
        print(x, liste_servs[x], liste_servs_ids[x])
    serveur = int(input(f"Merci d'entrer un nombre entre 0 et {len(liste_servs)} >>> "))
    data = {"servname" : liste_servs[serveur],
            "servid" : liste_servs_ids[serveur],
            "servobject" : bot.getguild(liste_servs_ids[serveur])}
    liste_channels = [channels.Channel(channel).name for channel in data["servobject"].getchannels().liste]
    liste_channels_ids = [channels.Channel(channel).id for channel in data["servobject"].getchannels().liste]
    liste_channels_objects = [channels.Channel(channel) for channel in data["servobject"].getchannels().liste]
    for x in range(len(liste_channels)):
        print(x, liste_channels[x], liste_channels_ids[x])
    channel = int(input(f"Merci d'entrer un nombre entre 0 et {len(liste_servs)} >>> "))
    data["channame"] = liste_channels[channel]
    data["chanid"] = liste_channels_ids[channel]
    data["chanobjet"] = liste_channels_objects[channel]
    print(data)

@pyscord.listener.event_on_ready
async def on_ready():
    print("démarrage du write_commands")
    change_serveur()

def interpreter(commande):
    global data
    if commande.startswith("/serveur"):
        change_serveur()
    else:
        bot.sendmessage(data["chanid"], commande)
        


while True:
    interpreter(input("COMMANDE >>> "))

bot.run()