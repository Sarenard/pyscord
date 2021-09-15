import requests
import channels
import messages
import client
import general

class User:
    def __init__(self, user, basic_header=None, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version
        self.raw = user
        self.item = user
        self.id = general.essai_element(user, "id")
        self.username = general.essai_element(user, "username")
        self.avatar = general.essai_element(user, "avatar")
        self.discriminator = general.essai_element(user, "discriminator")
        self.public_flags = general.essai_element(user, "public_flags")
        self.bot = general.essai_element(user, "bot")
        self.name = self.username + "#" + self.discriminator if self.username != None and self.discriminator != None else None