import pyscord
import sys

class Guild:
    def __init__(self, input, type=0):
        if type == 0:
            self.guild = input
            self.id = self.guild["id"]
            self.name = self.guild["name"]
            self.icon = self.guild["icon"]
            self.owner = self.guild["owner"]
            self.permissions = self.guild["permissions"]
            self.features = self.guild["features"]
        if type == 1:
            self.guild = input
            self.id = self.guild["id"]
            self.name = self.guild["name"]
            self.icon = self.guild["icon"]
            self.description = self.guild["description"]
            self.splash = self.guild["splash"]
            self.discovery_splash = self.guild["discovery_splash"]
            self.features = self.guild["features"]
            self.approximate_member_count = self.guild["approximate_member_count"]
            self.approximate_presence_count = self.guild["approximate_presence_count"]
            self.emojis = self.guild["emojis"]

class Guilds():
    def __init__(self, liste):
        self.liste = liste
    def getid(self, name):
        """
        récupère l'id d'un serveur a partir d'un nom, et si il y en a pas raise une Exception
        """
        for element in self.liste:
            if element["name"] == name:
                return int(element["id"])
        else:
            raise Exception("Il n'y a pas de serveurs avec ce nom !")
    def getguild(self, id):
        """
        récupère l'objet "Guild" a partir d'un id
        """
        for element in self.liste:
            if element["id"] == str(id):
                return Guild(element, 0)
        else:
            raise Exception("Il n'y a pas de serveurs avec cet id !")
    def getnames(self):
        """
        renvoie une liste de tout les noms de serveurs
        """
        liste_names = []
        for element in self.liste:
            liste_names.append(str(element["name"]))
        return liste_names
    def getids(self):
        """
        renvoie une liste de tout les id des serveurs
        """
        liste_id = []
        for element in self.liste:
            liste_id.append(str(element["id"]))
        return liste_id
    def getraw(self):
        """
        renvoie la liste brute
        """
        return self.liste
    def getfeatures(self):
        """
        renvoie la liste brute
        """
        liste_features = []
        for element in self.liste:
            liste_features.append(str(element["features"]))
        return liste_features