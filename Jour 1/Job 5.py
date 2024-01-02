class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Point: ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x): {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y): {self.y}")

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Exemple d'utilisation de la classe Point
point1 = Point(3, 5)

point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

point1.changerX(7)
point1.changerY(9)

point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()