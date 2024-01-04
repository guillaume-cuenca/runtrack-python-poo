class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    def ajouter_population(self, nombre):
        self.__habitants += nombre


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.ajouter_population(1)


# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage de la population initiale des villes
print(f"Population de la ville de {paris.get_nom()} : {paris.get_habitants()} habitants")
print(f"Population de la ville de {marseille.get_nom()} : {marseille.get_habitants()} habitants")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Mise à jour de la population des villes après l'arrivée des nouvelles personnes
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Affichage de la population mise à jour des villes
print(f"Mise à jour de la population de la ville de {paris.get_nom()} : {paris.get_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()} : {marseille.get_habitants()} habitants")