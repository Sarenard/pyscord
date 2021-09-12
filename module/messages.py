import requests
import channels
import pyscord
import general
import guild
import user

class Message:
    def __init__(self, message):
        self.raw = message
        self.id = message["id"]
        self.type = message["type"]
        self.content = message["content"]
        self.channel_id = message["channel_id"]
        self.author = user.User(message["author"])
        self.attachments = message["attachments"]
        self.embeds = message["embeds"]
        self.mentions = message["mentions"]
        self.mention_roles = message["mention_roles"]
        self.pinned = message["pinned"]
        self.mention_everyone = message["mention_everyone"]
        self.tts = message["tts"]
        self.timestamp = message["timestamp"]
        self.edited_timestamp = message["edited_timestamp"]
        self.flags = message["flags"]
        self.components = message["components"]
        self.referenced_message = message["referenced_message"]