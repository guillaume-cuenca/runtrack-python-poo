class Joueur:
    def __init__(self, nom, numéro, position):
        self.nom = nom
        self.numéro = numéro
        self.position = position
        self.buts_marqués = 0
        self.passes_décisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marqués += 1

    def effectuerUnePasseDecisive(self):
        self.passes_décisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom}:")
        print(f"   Numéro: {self.numéro}")
        print(f"   Position: {self.position}")
        print(f"   Buts marqués: {self.buts_marqués}")
        print(f"   Passes décisives: {self.passes_décisives}")
        print(f"   Cartons jaunes: {self.cartons_jaunes}")
        print(f"   Cartons rouges: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        joueur.buts_marqués += buts
        joueur.passes_décisives += passes
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges


# Création des joueurs
joueur1 = Joueur("Joueur1", 10, "Attaquant")
joueur2 = Joueur("Joueur2", 5, "Milieu")
joueur3 = Joueur("Joueur3", 3, "Défenseur")

# Création des équipes
equipe1 = Equipe("Équipe1")
equipe2 = Equipe("Équipe2")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques initiales des joueurs
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur(joueur1, buts=1)
equipe1.mettreAJourStatistiquesJoueur(joueur2, passes=1)
equipe2.mettreAJourStatistiquesJoueur(joueur3, cartons_jaunes=1)

# Affichage des statistiques après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()