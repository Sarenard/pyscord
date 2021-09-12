import requests
import pyscord
import guild

class Channel:
    def __init__(self, item, basic_header, api_version=9):
        self.raw = item
        self.item = item
        self.api_version = api_version
        self.basic_header = basic_header
    
class Channels:
    def __init__(self, liste, basic_header, api_version=9):
        self.raw = liste
        self.liste = liste
        self.api_version = api_version
        self.basic_header = basic_header