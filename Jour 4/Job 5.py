class Forme:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        super().__init__(0, 0)  # Un cercle n'a pas de largeur ni de hauteur, donc on initialise à 0
        self.radius = radius

    def aire(self):
        # La formule pour l'aire d'un cercle est π * r^2
        return 3.14 * self.radius ** 2

# Création d'une instance de la classe Rectangle
rectangle = Forme(5, 10)

# Création d'une instance de la classe Cercle
cercle = Cercle(7)

# Test des différentes surcharges de la méthode aire
print("Aire du rectangle:", rectangle.aire())  # Affiche 5 * 10 = 50
print("Aire du cercle:", cercle.aire())  # Affiche π * 7^2 ≈ 153.94