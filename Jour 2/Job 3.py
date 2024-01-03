class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def verification(self):
        """Vérifie si le livre est disponible."""
        return self.disponible

    def emprunter(self):
        """Emprunte le livre s'il est disponible."""
        if self.verification():
            print(f"Le livre '{self.titre}' a été emprunté.")
            self.disponible = False
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible.")

    def rendre(self):
        """Rend le livre s'il a été emprunté."""
        if not self.verification():
            print(f"Le livre '{self.titre}' a été rendu.")
            self.disponible = True
        else:
            print(f"Le livre '{self.titre}' n'a pas été emprunté.")

# Exemple d'utilisation
livre_exemple = Livre("Titre du Livre", "Auteur du Livre")

# Vérification de la disponibilité
print("Le livre est disponible :", livre_exemple.verification())

# Emprunt du livre
livre_exemple.emprunter()

# Tentative d'emprunt du livre à nouveau
livre_exemple.emprunter()

# Rendre le livre
livre_exemple.rendre()

# Tentative de rendre le livre à nouveau
livre_exemple.rendre()