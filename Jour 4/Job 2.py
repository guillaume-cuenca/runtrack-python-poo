class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence.")

# Création d'un élève
eleve1 = Eleve(nom="Jean", age=15)

# Appel des méthodes demandées pour l'élève
eleve1.bonjour()
eleve1.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
eleve1.age = 15

# Création d'un professeur
professeur1 = Professeur(nom="Professeur Smith", age=40)

# Appel des méthodes demandées pour le professeur
professeur1.bonjour()
professeur1.enseigner()