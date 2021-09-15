import requests
import channels
import client
import general
import guild
import user

class Message:
    def __init__(self, message):
        self.raw = message
        self.id = general.essai_element(message, "id")
        self.channel_id = general.essai_element(message, "channel_id")
        self.guild_id = general.essai_element(message, "guild_id")
        self.author = user.User(general.essai_element(message, "author"))
        self.member = general.essai_element(message, "member")
        self.content = general.essai_element(message, "content")
        self.timestamp = general.essai_element(message, "timestamp")
        self.edited_timestamp = general.essai_element(message, "edited_timestamp")
        self.tts = general.essai_element(message, "tts")
        self.mention_everyone = general.essai_element(message, "mention_everyone")
        self.mentions = general.essai_element(message, "mentions")
        self.mention_roles = general.essai_element(message, "mention_roles")
        self.mention_channels = general.essai_element(message, "mention_channels")
        self.attachments = general.essai_element(message, "attachments")
        self.embeds = general.essai_element(message, "embeds")
        self.reactions = general.essai_element(message, "reactions")
        self.nonce = general.essai_element(message, "nonce")
        self.pinned = general.essai_element(message, "pinned")
        self.webhook_id = general.essai_element(message, "webhook_id")
        self.type = general.essai_element(message, "type")
        self.activity = general.essai_element(message, "activity")
        self.application = general.essai_element(message, "application")
        self.application_id = general.essai_element(message, "application_id")
        self.message_reference = general.essai_element(message, "message_reference")
        self.flags = general.essai_element(message, "flags")
        self.referenced_message = general.essai_element(message, "referenced_message")
        self.interaction = general.essai_element(message, "interaction")
        self.thread = general.essai_element(message, "thread")
        self.components = general.essai_element(message, "components")
        self.sticker_items = general.essai_element(message, "sticker_items")
        self.stickers = general.essai_element(message, "stickers")