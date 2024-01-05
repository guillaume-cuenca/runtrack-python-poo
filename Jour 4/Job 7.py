import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.points = self.attribuer_points()

    def attribuer_points(self):
        if self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11  # Note: L'As peut valoir 11 ou 1, la logique pour choisir est ajoutée plus tard
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self, nombre_cartes=2):
        cartes = []
        for _ in range(nombre_cartes):
            carte = self.paquet.pop()
            cartes.append(carte)
        return cartes

# Création du jeu
jeu = Jeu()
jeu.melanger_paquet()

# Distribution des cartes au joueur et au croupier
main_joueur = jeu.distribuer_cartes()
main_croupier = jeu.distribuer_cartes()

print("Main du joueur:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

print("\nMain du croupier:")
print(f"{main_croupier[0].valeur} de {main_croupier[0].couleur} (une carte cachée)")

# Le joueur prend des cartes supplémentaires (exemple avec une seule carte)
main_joueur += jeu.distribuer_cartes(1)

print("\nMain du joueur après avoir pris une carte supplémentaire:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

# Le joueur passe au croupier
while sum([carte.points for carte in main_croupier]) < 17:
    main_croupier += jeu.distribuer_cartes(1)

print("\nMain finale du croupier:")
for carte in main_croupier:
    print(f"{carte.valeur} de {carte.couleur}")

# Vérifier le résultat
total_joueur = sum([carte.points for carte in main_joueur])
total_croupier = sum([carte.points for carte in main_croupier])

if total_joueur > 21:
    print("\nLe joueur a dépassé 21. Le croupier gagne.")
elif total_croupier > 21:
    print("\nLe croupier a dépassé 21. Le joueur gagne.")
elif total_joueur > total_croupier:
    print("\nLe joueur gagne.")
elif total_croupier > total_joueur:
    print("\nLe croupier gagne.")
else:
    print("\nÉgalité.")