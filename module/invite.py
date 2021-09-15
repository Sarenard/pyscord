import channels
import client
import general
import guild
import invite
import listener
import messages
import user

class Invite:
    def __init__(self, invite, basic_header, api_version=9):
        self.basic_header = basic_header
        self.api_version = api_version

        self.raw = invite
        self.invite = invite

        self.code = general.essai_element(invite, "code")
        self.guild = guild.Guild(general.essai_element(invite, "guild"), api_version=self.api_version, basic_header=self.basic_header)
        self.channel = channels.Channel(general.essai_element(invite, "channel"), api_version=self.api_version, basic_header=self.basic_header)
        self.inviter = user.User(general.essai_element(invite, "inviter"), api_version=self.api_version, basic_header=self.basic_header)
        self.target_type = general.essai_element(invite, "target_type")
        self.target_user = user.User(general.essai_element(invite, "target_user"), api_version=self.api_version, basic_header=self.basic_header)
        self.target_application = general.essai_element(invite, "target_application")
        self.approximate_presence_count = general.essai_element(invite, "approximate_presence_count")
        self.approximate_member_count = general.essai_element(invite, "approximate_member_count")
        self.expires_at = general.essai_element(invite, "expires_at")
        self.stage_instance = general.essai_element(invite, "stage_instance")