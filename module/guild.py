import requests
import pyscord
import json
import sys

class Guild:
    def __init__(self, input, basic_header, type=0, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version
        self.guild = input
        self.raw = input
        self.id = self.guild["id"]
        self.type = type
        if type == 0: #normal
            self.name = self.guild["name"]
            self.icon = self.guild["icon"]
            self.owner = self.guild["owner"]
            self.permissions = self.guild["permissions"]
            self.features = self.guild["features"]
        if type == 1: #preview
            self.name = self.guild["name"]
            self.icon = self.guild["icon"]
            self.description = self.guild["description"]
            self.splash = self.guild["splash"]
            self.discovery_splash = self.guild["discovery_splash"]
            self.features = self.guild["features"]
            self.approximate_member_count = self.guild["approximate_member_count"]
            self.approximate_presence_count = self.guild["approximate_presence_count"]
            self.emojis = self.guild["emojis"]
        if type == 2: #get de base
            self.name = self.guild["name"]
            self.icon = self.guild["icon"]
            self.description = self.guild["description"]
            self.splash = self.guild["splash"]
            self.discovery_splash = self.guild["discovery_splash"]
            self.features = self.guild["features"]
            self.emojis = self.guild["emojis"]
            self.stickers = self.guild["stickers"]
            self.banner = self.guild["banner"]
            self.owner_id = self.guild["owner_id"]
            self.application_id = self.guild["application_id"]
            self.region = self.guild["region"]
            self.afk_channel_id = self.guild["afk_channel_id"]
            self.afk_timeout = self.guild["afk_timeout"]
            self.system_channel_id = self.guild["system_channel_id"]
            self.widget_enabled = self.guild["widget_enabled"]
            self.widget_channel_id = self.guild["widget_channel_id"]
            self.verification_level = self.guild["verification_level"]
            self.roles = self.guild["roles"]
            self.default_message_notifications = self.guild["default_message_notifications"]
            self.mfa_level = self.guild["mfa_level"]
            self.explicit_content_filter = self.guild["explicit_content_filter"]
            self.max_presences = self.guild["max_presences"]
            self.max_members = self.guild["max_members"]
            self.max_video_channel_users = self.guild["max_video_channel_users"]
            self.vanity_url_code = self.guild["vanity_url_code"]
            self.premium_tier = self.guild["premium_tier"]
            self.premium_subscription_count = self.guild["premium_subscription_count"]
            self.system_channel_flags = self.guild["system_channel_flags"]
            self.preferred_locale = self.guild["preferred_locale"]
            self.rules_channel_id = self.guild["rules_channel_id"]
            self.public_updates_channel_id = self.guild["public_updates_channel_id"]
            self.nsfw = self.guild["nsfw"]
            self.nsfw_level = self.guild["nsfw_level"]
        if type == 3: #get de base
            self.raw = input
    def getpreview(self):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}/preview"
        return Guild(json.loads(requests.get(url, headers=self.basic_header).text), type=1, api_version=self.api_version, basic_header=self.basic_header)
    def modify(self, json):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}"
        return Guild(requests.patch(url, headers=self.basic_header, json=json).json(), type=2, api_version=self.api_version, basic_header=self.basic_header)

class Guilds():
    def __init__(self, liste, basic_header, api_version=9):
        self.liste = liste
        self.api_version = api_version
        self.basic_header = basic_header
    def getid(self, name):
        """
        récupère l'id d'un serveur a partir d'un nom, et si il y en a pas raise une Exception
        """
        for element in self.liste:
            if element["name"] == name:
                return int(element["id"])
        else:
            raise Exception("Il n'y a pas de serveurs avec ce nom !")
    def getguild(self, id):
        """
        récupère l'objet "Guild" a partir d'un id
        """
        for element in self.liste:
            if element["id"] == str(id):
                return Guild(element, type=0, api_version=self.api_version, basic_header=self.basic_header)
        else:
            raise Exception("Il n'y a pas de serveurs avec cet id !")
    def getnames(self):
        """
        renvoie une liste de tout les noms de serveurs
        """
        liste_names = []
        for element in self.liste:
            liste_names.append(str(element["name"]))
        return liste_names
    def getids(self):
        """
        renvoie une liste de tout les id des serveurs
        """
        liste_id = []
        for element in self.liste:
            liste_id.append(str(element["id"]))
        return liste_id
    def getraw(self):
        """
        renvoie la liste brute
        """
        return self.liste
    def getfeatures(self):
        """
        renvoie la liste brute
        """
        liste_features = []
        for element in self.liste:
            liste_features.append(str(element["features"]))
        return liste_features