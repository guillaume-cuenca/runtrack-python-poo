import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        joueur = Personnage("Joueur", 100 + self.niveau * 10)
        ennemi = Personnage("Ennemi", 50 + self.niveau * 5)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            print(f"\n{ joueur.nom } - Vie: { joueur.vie } | { ennemi.nom } - Vie: { ennemi.vie }\n")

        self.verifierGagnant(joueur, ennemi)

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie <= 0:
            print(f"{ ennemi.nom } a gagné !")
        else:
            print(f"{ joueur.nom } a gagné !")

# Exemple d'utilisation
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()