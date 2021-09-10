import requests
import json
import ast

import getguild

class Client():
    def __init__(self, token):
        self.token = token
    def getguilds(self):
        url = "https://discord.com/api/v8/users/@me/guilds"
        headers = {
            "Authorization": f"Bot {self.token}"
        }
        return getguild.Guilds(json.loads(requests.get(url, headers=headers).text))
    def getpreview(self, id):
        url = f"https://discord.com/api/v9//guilds/{id}/preview"
        headers = {
            "Authorization": f"Bot {self.token}"
        }
        return getguild.Guild(json.loads(requests.get(url, headers=headers).text), 1)

        