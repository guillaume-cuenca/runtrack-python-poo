class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}  # Dictionnaire pour stocker les plats commandés
        self._statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self._plats_commandes:
            self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self._statut_commande}
            print(f"Plat {nom_plat} ajouté à la commande {self._numero_commande}.")

    def annuler_commande(self):
        self._statut_commande = "annulée"
        print(f"Commande {self._numero_commande} annulée.")

    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande {self._numero_commande} - Statut : {self._statut_commande}")
        for plat, details in self._plats_commandes.items():
            print(f"{plat}: {details['prix']} € - Statut: {details['statut']}")
        print(f"Total à payer : {self._calculer_total()} € (TVA incluse)")

    def calculer_tva(self, taux_tva):
        tva = self._calculer_total() * (taux_tva / 100)
        print(f"TVA ({taux_tva}%): {tva} €")

# Exemple d'utilisation de la classe
commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Pizza", 10.99)
commande1.ajouter_plat("Pâtes", 7.50)
commande1.afficher_commande()
commande1.calculer_tva(taux_tva=10)

commande1.annuler_commande()
commande1.afficher_commande()