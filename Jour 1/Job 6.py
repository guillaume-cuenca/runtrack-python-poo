class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
print("L'age de l'animal", mon_animal.age, "ans")

# Appel de la méthode vieillir
mon_animal.vieillir()

# Affichage de l'âge de l'animal après avoir vieilli
print("L'age de l'animal", mon_animal.age, "ans")

# Appel de la méthode nommer
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print("L'animal se nomme", mon_animal.prenom)