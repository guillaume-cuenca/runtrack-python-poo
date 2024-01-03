class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # ajout de l'attribut reservoir avec une valeur par défaut

    # Mutateurs et assesseurs pour chaque attribut
    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return self.__en_marche

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")

    # Méthode privée pour vérifier le niveau du réservoir
    def verifier_plein(self):
        return self.__reservoir > 5

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "Camry", 2020, 30000)

# Affichage des informations de la voiture
print(f"Marque: {ma_voiture.get_marque()}")
print(f"Modèle: {ma_voiture.get_modele()}")
print(f"Année: {ma_voiture.get_annee()}")
print(f"Kilométrage: {ma_voiture.get_kilometrage()} km")
print(f"En marche: {ma_voiture.get_en_marche()}")

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()