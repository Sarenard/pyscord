import requests
import listener
import channels
import messages
import general
import guild
import user

class RoleTag:
    def __init__(self, role):
        self.raw = role
        self.bot_id = general.essai_element(role, "bot_id")
        self.integration_id = general.essai_element(role, "integration_id")
        self.premium_subscriber = general.essai_element(role, "premium_subscriber")

class Role:
    def __init__(self, role):
        self.raw = role
        self.id = general.essai_element(role, "id")
        self.name = general.essai_element(role, "name")
        self.color = general.essai_element(role, "color")
        self.hoist = general.essai_element(role, "hoist")
        self.position = general.essai_element(role, "position")
        self.permissions = general.essai_element(role, "permissions")
        self.managed = general.essai_element(role, "managed")
        self.mentionable = general.essai_element(role, "mentionable")
        self.tags = RoleTag(general.essai_element(role, "tags"))