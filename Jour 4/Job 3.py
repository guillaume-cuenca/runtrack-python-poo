class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, value):
        self._largeur = value

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        self._hauteur = value

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


# Instanciation de la classe Rectangle
rectangle1 = Rectangle(5, 10)

# Utilisation des méthodes de la classe Rectangle
print("Périmètre du rectangle:", rectangle1.perimetre())
print("Surface du rectangle:", rectangle1.surface())

# Modification des attributs à l'aide des mutateurs
rectangle1.longueur = 8
rectangle1.largeur = 12

# Affichage des attributs mis à jour
print("Nouvelle longueur du rectangle:", rectangle1.longueur)
print("Nouvelle largeur du rectangle:", rectangle1.largeur)

# Instanciation de la classe Parallelepipede
parallelepipede1 = Parallelepipede(3, 4, 5)

# Utilisation des méthodes de la classe Parallelepipede
print("Volume du parallélépipède:", parallelepipede1.volume())