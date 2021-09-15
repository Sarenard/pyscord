import requests
import channels
import messages
import client
import general
import roles
import user
import sys

class Guild:
    def __init__(self, guild, basic_header, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version
        self.raw = guild
        self.guild = guild

        self.id = general.essai_element(guild, "id")
        self.name = general.essai_element(guild, "name")
        self.icon = general.essai_element(guild, "icon")
        self.icon_hash = general.essai_element(guild, "icon_hash")
        self.splash = general.essai_element(guild, "splash")
        self.discovery_splash = general.essai_element(guild, "discovery_splash")
        self.owner = general.essai_element(guild, "owner")
        self.owner_id = general.essai_element(guild, "owner_id")
        self.permissions = general.essai_element(guild, "permissions")
        self.region = general.essai_element(guild, "region")
        self.afk_channel_id = general.essai_element(guild, "afk_channel_id")
        self.afk_timeout = general.essai_element(guild, "afk_timeout")
        self.widget_enabled = general.essai_element(guild, "widget_enabled")
        self.widget_channel_id = general.essai_element(guild, "widget_channel_id")
        self.verification_level = general.essai_element(guild, "verification_level")
        self.default_message_notifications = general.essai_element(guild, "default_message_notifications")
        self.explicit_content_filter = general.essai_element(guild, "explicit_content_filter")
        try: self.roles = [roles.Role(role) for role in general.essai_element(guild, "roles")]
        except: pass
        self.emojis = general.essai_element(guild, "emojis")
        self.features = general.essai_element(guild, "features")
        self.mfa_level = general.essai_element(guild, "mfa_level")
        self.application_id = general.essai_element(guild, "application_id")
        self.system_channel_id = general.essai_element(guild, "system_channel_id")
        self.system_channel_flags = general.essai_element(guild, "system_channel_flags")
        self.rules_channel_id = general.essai_element(guild, "rules_channel_id")
        self.joined_at = general.essai_element(guild, "joined_at")
        self.large = general.essai_element(guild, "large")
        self.unavailable = general.essai_element(guild, "unavailable")
        self.member_count = general.essai_element(guild, "member_count")
        self.voice_states = general.essai_element(guild, "voice_states")
        self.members = general.essai_element(guild, "members")
        self.channels = general.essai_element(guild, "channels")
        try: self.channels = [channels.Channel(role, basic_header=self.basic_header, api_version=self.api_version) for channel in general.essai_element(guild, "channels")]
        except: pass
        self.threads = general.essai_element(guild, "threads")
        self.presences = general.essai_element(guild, "presences")
        self.max_presences = general.essai_element(guild, "max_presences")
        self.max_members = general.essai_element(guild, "max_members")
        self.vanity_url_code = general.essai_element(guild, "vanity_url_code")
        self.description = general.essai_element(guild, "description")
        self.banner = general.essai_element(guild, "banner")
        self.premium_tier = general.essai_element(guild, "premium_tier")
        self.premium_subscription_count = general.essai_element(guild, "premium_subscription_count")
        self.preferred_locale = general.essai_element(guild, "preferred_locale")
        self.public_updates_channel_id = general.essai_element(guild, "public_updates_channel_id")
        self.max_video_channel_users = general.essai_element(guild, "max_video_channel_users")
        self.approximate_member_count = general.essai_element(guild, "approximate_member_count")
        self.approximate_presence_count = general.essai_element(guild, "approximate_presence_count")
        self.welcome_screen = general.essai_element(guild, "welcome_screen")
        self.nsfw_level = general.essai_element(guild, "nsfw_level")
        self.stage_instances = general.essai_element(guild, "stage_instances")
        self.stickers = general.essai_element(guild, "stickers")

    def getpreview(self):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}/preview"
        return Guild(requests.get(url, headers=self.basic_header).json(), api_version=self.api_version, basic_header=self.basic_header)
    def modify(self, json):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}"
        return Guild(requests.patch(url, headers=self.basic_header, json=json).json(), api_version=self.api_version, basic_header=self.basic_header)
    def delete(self):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}"
        if requests.delete(url, headers=self.basic_header).json() == {'message': 'Missing Access', 'code': 50001}:
            raise Exception(f"Le bot ne peut pas supprimer le serveur {self.id}, il n'en est pas l'owner")
        else:
            return True
    def getchannels(self):
        url = f"https://discord.com/api/v{self.api_version}/guilds/{self.id}/channels"
        return channels.Channels(requests.get(url, headers=self.basic_header).json(), basic_header=self.basic_header)
    def getchannel(self, id):
        url = f"https://discord.com/api/v{self.api_version}/channels/{id}"
        return channels.Channel(requests.get(url, headers=self.basic_header).json(), basic_header=self.basic_header)
        

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
                return Guild(element, api_version=self.api_version, basic_header=self.basic_header)
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