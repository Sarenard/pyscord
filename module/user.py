import requests
import channels
import messages
import pyscord
import general

class User:
    def __init__(self, user):
        self.raw = user
        self.item = user
        self.id = general.essai_element(user, "id")
        self.username = general.essai_element(user, "username")
        self.avatar = general.essai_element(user, "avatar")
        self.discriminator = general.essai_element(user, "discriminator")
        self.public_flags = general.essai_element(user, "public_flags")
        self.bot = general.essai_element(user, "bot")
        