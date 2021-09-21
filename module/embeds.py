import requests
import channels
import client
import general
import guild
import user

class EmbedFooter:
    def __init__(self, text, **kwargs):
        self.text = text
        self.icon_url = kwargs.get("icon_url", None)
        self.proxy_icon_url = kwargs.get("proxy_icon_url", None)
        
    
class EmbedImage:
    def __init__(self, url, **kwargs):
        self.url = url
        self.proxy_url = kwargs.get("proxy_url", None)
        self.height = kwargs.get("height", 0)
        self.width = kwargs.get("width", 0)
    
class EmbedThumbnail:
    def __init__(self, url, **kwargs):
        self.url = url
        self.proxy_url = kwargs.get("proxy_url", None)
        self.height = kwargs.get("height", 0)
        self.width = kwargs.get("width", 0)
    
class EmbedVideo:
    def __init__(self, url, **kwargs):
        self.url = url
        self.proxy_url = kwargs.get("proxy_url", None)
        self.height = kwargs.get("height", 0)
        self.width = kwargs.get("width", 0)
    
class EmbedProvider:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.url = kwargs.get("url", None)
    
class EmbedAuthor:
    def __init__(self, name, **kwargs):
        self.name = name
        self.url = kwargs.get("url", None)
        self.icon_url = kwargs.get("icon_url", None)
        self.proxy_icon_url = kwargs.get("proxy_icon_url", None)
    
class EmbedField:
    def __init__(self, name, value, **kwargs):
        self.name = name
        self.value = value
        self.inline = kwargs.get("inline", False)

class Embed:
    def __init__(self, titre, **kwargs):
        self.title = titre
        self.type = kwargs.get("type", "")
        self.description = kwargs.get("description", "")
        self.url = kwargs.get("url", "")
        self.timestamp = kwargs.get("timestamp", 0)
        self.color = kwargs.get("color", 0)
        self.footer = kwargs.get("footer", None)
        self.image = kwargs.get("image", None)
        self.thumbnail = kwargs.get("thumbnail", None)
        self.video = kwargs.get("video", None)
        self.provider = kwargs.get("provider", None)
        self.author = kwargs.get("author", None)
        self.fields = []
    def settitre(self, titre):
        self.titre = titre
    def settype(self, type):
        self.type = type
    def setdescription(self, description):
        self.description = description
    def seturl(self, url):
        self.url = url
    def settimestamp(self, timestamp):
        self.timestamp = timestamp
    def setcolor(self, color):
        self.color = color
    #TODO : rajouter les class footer, image, thubmnail, video, provider et author dans Embed()
    def getraw(self):
        #TODO : faire le getraw
        pass