import requests
import channels
import messages
import pyscord
import general

class User:
    def __init__(self, user, basic_header, api_version=9):
        self.raw = user
        self.item = user
        self.api_version = api_version
        self.basic_header = basic_header
        self.id = general.essai_element(user, "id")
        self.username = general.essai_element(user, "username")
        self.avatar = general.essai_element(user, "avatar")
        self.discriminator = general.essai_element(user, "discriminator")
        self.public_flags = general.essai_element(user, "public_flags")
        self.bot = general.essai_element(user, "bot")
        