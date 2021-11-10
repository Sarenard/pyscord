import threading
import requests
import listener
import channels
import messages
import general
import embeds
import invite
import guild
import user
import time
import ast
import sys
import os

class Client():
    def __init__(self, token, id, api_version=9):
        self.token = token
        self.basic_header = {"Authorization": f"Bot {self.token}"}
        self.api_version = api_version
        self.id = id
        self.listener = listener.Listener(self.token, basic_head=self.basic_header, api_ver=self.api_version, id = self.id)
        
    def deleteguild(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}"
        requests.delete(url, headers=self.basic_header)
        return True

    def createguild(self, name):
        json = {"name" : name}
        url = f"https://discord.com/api/v{self.api_version}/guilds"
        return guild.Guild(requests.post(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)

    def getguilds(self):
        url = f"https://discord.com/api/v{self.api_version}/users/@me/guilds"
        return guild.Guilds(requests.get(url, headers=self.basic_header).json(), api_version=self.api_version, basic_header=self.basic_header)
    
    def getguild(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}"
        return guild.Guild(requests.get(url, headers=self.basic_header).json(), api_version=self.api_version, basic_header=self.basic_header)
    
    def getchannel(self, id):
        url = f"https://discord.com/api/v{self.api_version}/channels/{id}"
        return channels.Channel(requests.get(url, headers=self.basic_header).json(), api_version=self.api_version, basic_header=self.basic_header)

    def getuser(self, id):
        url = f"https://discord.com/api/v{self.api_version}/users/{user.id}"
        return user.User(requests.get(url, headers=self.basic_header).json(), api_version=self.api_version, basic_header=self.basic_header)
    
    def sendmessage(self, id, content, embed=None, json={}):
        if json == {} and embed is None: json = {"content" : content}
        if json == {} and embed != None : json = {"content" : content, embeds : [embed.getraw()]}
        url = f"https://discord.com/api/v{self.api_version}/channels/{id}/messages"
        return messages.Message(requests.post(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)
    
    def reply(self, message, content, json={}):
        if json == {} : json = {"content" : content}
        url = f"https://discord.com/api/v{self.api_version}/channels/{message.channel_id}/messages"
        return messages.Message(requests.post(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)

    def modify(self, json):
        url = f"https://discord.com/api/v{self.api_version}/users/@me"
        return user.User(requests.patch(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)

    def changename(self, name):
        return self._extracted_from_changeavatar_2("username", name)
        
    def changeavatar(self, avatar):
        return self._extracted_from_changeavatar_2("avatar", avatar)

    # TODO Rename this here and in `changename` and `changeavatar`
    def _extracted_from_changeavatar_2(self, arg0, arg1):
        json = {arg0: arg1}
        url = f'https://discord.com/api/v{self.api_version}/users/@me'
        return user.User(
            requests.patch(url, headers=self.basic_header, json=json).json(),
            api_version=self.api_version,
            basic_header=self.basic_header,
        )

    def createinvite(self, channel_id, json={}):
        url = f"https://discord.com/api/v{self.api_version}/channels/{channel_id}/invites"
        return invite.Invite(requests.post(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)

    def run(self):
        self.listener.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.listener.stop()
            print("Arret du bot")
            os._exit(1)
