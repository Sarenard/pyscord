import requests
import messages
import general
import invite
import client
import guild
import user

class Channel:
    def __init__(self, item, basic_header=None, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version

        self.raw = item
        self.item = item
        self.id = general.essai_element(item, "id")
        self.name = general.essai_element(item, "name")
    def sendmessage(self, content, json={}):
        if json == {} : json = {"content" : content}
        url = f"https://discord.com/api/v{self.api_version}/channels/{self.id}/messages"
        return messages.Message(requests.post(url, headers=self.basic_header, api_version=self.api_version, json=json).json())
    def createinvite(self, json={}):
        url = f"https://discord.com/api/v{self.api_version}/channels/{self.id}/invites"
        return invite.Invite(requests.post(url, headers=self.basic_header, api_version=self.api_version, json=json).json())
    
class Channels:
    def __init__(self, liste, basic_header, api_version=9):
        self.raw = liste
        self.liste = liste
        self.api_version = api_version
        self.basic_header = basic_header