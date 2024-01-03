class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

    # Assesseurs
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nb_pages(self):
        return self._nb_pages

    # Mutateurs
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre

    def set_auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        # Vérifier si le nombre de pages est un entier positif
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self._nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Exemple d'utilisation
livre1 = Livre("Titre du Livre", "Auteur du Livre", 200)
print("Titre:", livre1.get_titre())
print("Auteur:", livre1.get_auteur())
print("Nombre de pages:", livre1.get_nb_pages())

# Modification des attributs
livre1.set_titre("Nouveau Titre")
livre1.set_auteur("Nouvel Auteur")
livre1.set_nb_pages(300)  # Modification réussie

# Affichage après modification
print("\nAprès modification:")
print("Titre:", livre1.get_titre())
print("Auteur:", livre1.get_auteur())
print("Nombre de pages:", livre1.get_nb_pages())

# Tentative de modification avec un nombre de pages non valide
livre1.set_nb_pages(-50)  # Affiche un message d'erreur
print("Nombre de pages après tentative de modification:", livre1.get_nb_pages())