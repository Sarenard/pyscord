import requests
import json
import ast

import guild

class Client():
    def __init__(self, token, api_version=9):
        self.token = token
        self.basic_header = {"Authorization": f"Bot {self.token}"}
        self.api_version = api_version
        
    def getguilds(self):
        url = f"https://discord.com/api/v{self.api_version}/users/@me/guilds"
        return guild.Guilds(json.loads(requests.get(url, headers=self.basic_header).text))
    
    def getguild(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}"
        return guild.Guild(json.loads(requests.get(url, headers=self.basic_header).text), 2)
    
    def getpreview(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}/preview"
        return guild.Guild(json.loads(requests.get(url, headers=self.basic_header).text), 1)
    