class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation
# Créer un personnage avec une position initiale (0, 0)
mon_personnage = Personnage(0, 0)

# Déplacer le personnage vers la droite et vers le haut
mon_personnage.droite()
mon_personnage.haut()

# Obtenir la position actuelle du personnage
position_actuelle = mon_personnage.position()

# Afficher la position
print("Position actuelle du personnage :", position_actuelle)