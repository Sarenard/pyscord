import requests
import messages
import general
import invite
import client
import guild
import user

class Channel:
    def __init__(self, item, basic_header=None, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version

        self.raw = item
        self.item = item
        self.id = general.essai_element(item, "id")
        self.type = general.essai_element(item, "type")
        self.guild_id = general.essai_element(item, "guild_id")
        self.position = general.essai_element(item, "position")
        self.permission_overwrites = general.essai_element(item, "permission_overwrites")
        self.name = general.essai_element(item, "name")
        self.topic = general.essai_element(item, "topic")
        self.nsfw = general.essai_element(item, "nsfw")
        self.last_message_id = general.essai_element(item, "last_message_id")
        self.bitrate = general.essai_element(item, "bitrate")
        self.user_limit = general.essai_element(item, "user_limit")
        self.rate_limit_per_user = general.essai_element(item, "rate_limit_per_user")
        try : self.recipients = [user.User(user) for user in general.essai_element(item, "dummy")]
        except : self.recipients = None
        self.icon = general.essai_element(item, "icon")
        self.owner_id = general.essai_element(item, "owner_id")
        self.application_id = general.essai_element(item, "application_id")
        self.parent_id = general.essai_element(item, "parent_id")
        self.last_pin_timestamp = general.essai_element(item, "last_pin_timestamp")
        self.rtc_region = general.essai_element(item, "rtc_region")
        self.video_quality_mode = general.essai_element(item, "video_quality_mode")
        self.message_count = general.essai_element(item, "message_count")
        self.member_count = general.essai_element(item, "member_count")
        self.thread_metadata = general.essai_element(item, "thread_metadata")
        self.member = general.essai_element(item, "member")
        self.default_auto_archive_duration = general.essai_element(item, "default_auto_archive_duration")
        self.permissions = general.essai_element(item, "permissions")


    def sendmessage(self, content, json={}):
        if json == {} : json = {"content" : content}
        url = f"https://discord.com/api/v{self.api_version}/channels/{self.id}/messages"
        return messages.Message(requests.post(url, headers=self.basic_header, api_version=self.api_version, json=json).json())
    def createinvite(self, json={}):
        url = f"https://discord.com/api/v{self.api_version}/channels/{self.id}/invites"
        return invite.Invite(requests.post(url, headers=self.basic_header, api_version=self.api_version, json=json).json())
    
class Channels:
    def __init__(self, liste, basic_header, api_version=9):
        self.raw = liste
        self.liste = liste
        self.api_version = api_version
        self.basic_header = basic_header