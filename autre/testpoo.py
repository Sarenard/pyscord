class Nombre:
    def __init__(self, nombre):
        self.nombre=nombre

    def __eq__(self, autre):
        #définit l'égalité entre 2 instances de Nombre
        #si leur 2 valeurs sont identiques
        return self.nombre == autre.nombre

    def add1(self):
        #ajoute 1 a l'élément "nombre"
        self.nombre += 1

un1 = Nombre(1)
un2 = Nombre(1)
print(un1 == un2)
un2.add1()
print(un1 == un2)
un1.add1()
print(un1 == un2)