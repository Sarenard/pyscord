import requests
import json
import ast

import guild

class Client():
    def __init__(self, token, api_version=9):
        self.token = token
        self.basic_header = {"Authorization": f"Bot {self.token}"}
        self.api_version = api_version
        
    def deleteguild(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}"
        return requests.delete(url, headers=self.basic_header)

    def createguild(self, name):
        url = f"https://discord.com/api/v{self.api_version}/guilds"
        return guild.Guild(requests.post(url, headers=self.basic_header, json=json).text, type=3, api_version=self.api_version, basic_header=self.basic_header)

    def getguilds(self):
        url = f"https://discord.com/api/v{self.api_version}/users/@me/guilds"
        return guild.Guilds(json.loads(requests.get(url, headers=self.basic_header).text), api_version=self.api_version, basic_header=self.basic_header)
    
    def getguild(self, id):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{id}"
        return guild.Guild(json.loads(requests.get(url, headers=self.basic_header).text), type=2, api_version=self.api_version, basic_header=self.basic_header)