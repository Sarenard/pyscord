import requests
import listener
import channels
import messages
import general
import guild
import user

class Role:
    def __init__(self, role):
        self.raw = role