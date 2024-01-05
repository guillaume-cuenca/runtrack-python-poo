class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}\nModel = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print("Voiture démarrée. En route!")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roues}")

    def demarrer(self):
        print("Moto démarrée. Prêt à rouler!")


# Instanciation de la classe Voiture
voiture_mercedes = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)
voiture_mercedes.informationsVehicule()

# Instanciation de la classe Moto
moto_yamaha = Moto(marque="Yamaha", modele="1200 VMax", annee=1987, prix=4500)
moto_yamaha.informationsVehicule()

# Tester la méthode demarrer
voiture_mercedes.demarrer()
moto_yamaha.demarrer()