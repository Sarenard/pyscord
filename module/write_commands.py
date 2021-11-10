import important
import channels
import pyscord

bot = pyscord.Client(token=important.token)

global data
data = ""

def change_serveur():
    global data
    listetemp = [bot.getguild(id) for id in bot.getguilds().getids()]
    liste_servs = [str(guild.name) for guild in listetemp]
    liste_servs_ids = [str(guild.id) for guild in listetemp]
    for x in range(len(liste_servs)):
        print(x, liste_servs[x], liste_servs_ids[x])
    serveur = int(input(f"Merci d'entrer un nombre entre 0 et {len(liste_servs)-1} >>> "))
    data = {"servname" : liste_servs[serveur],
            "servid" : liste_servs_ids[serveur],
            "servobject" : bot.getguild(liste_servs_ids[serveur]),
            "listechannels" : bot.getguild(liste_servs_ids[serveur]).getchannels().liste}
    liste_channels = [channels.Channel(channel).name for channel in data["listechannels"]]
    liste_channels_ids = [channels.Channel(channel).id for channel in data["listechannels"]]
    liste_channels_objects = [channels.Channel(channel) for channel in data["listechannels"]]
    for x in range(len(liste_channels)):
        print(x, liste_channels[x], liste_channels_ids[x])
    channel = int(input(f"Merci d'entrer un nombre entre 0 et {len(liste_channels)-1} >>> "))
    data["channame"] = liste_channels[channel]
    data["chanid"] = liste_channels_ids[channel]
    data["chanobjet"] = liste_channels_objects[channel]

@pyscord.listener.event_on_ready
async def on_ready():
    global data
    print("démarrage du write_commands")
    change_serveur()

while True:
    commande = input("COMMANDE >>> ")
    if commande.startswith("/serveur"):
        change_serveur()
    elif not commande.startswith("/"):
        bot.sendmessage(data["chanid"], commande)



while True:
    interpreter(input("COMMANDE >>> "))

bot.run()