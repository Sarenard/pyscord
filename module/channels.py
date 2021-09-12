import requests
import messages
import pyscord
import general
import guild
import user

class Channel:
    def __init__(self, item, basic_header, api_version=9):
        self.raw = item
        self.item = item
        self.api_version = api_version
        self.basic_header = basic_header
        self.id = item["id"]
    def sendmessage(self, content, json={}):
        if json == {} : json = {"content" : content}
        url = f"https://discord.com/api/v{self.api_version}/channels/{self.id}/messages"
        return messages.Message(requests.post(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)
    
class Channels:
    def __init__(self, liste, basic_header, api_version=9):
        self.raw = liste
        self.liste = liste
        self.api_version = api_version
        self.basic_header = basic_header