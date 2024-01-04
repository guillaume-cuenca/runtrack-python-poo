class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n° {self.__numero_compte} - {self.__nom} {self.__prenom}")
        print(f"Solde: {self.__solde} €")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} € ont été appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte n° {compte_destinataire.__numero_compte}")
        else:
            print("Opération impossible. Solde insuffisant.")

# Création d'une première instance de la classe
compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde=1000)

# Appel des différentes méthodes
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)

# Ajout de l'attribut decouvert à True pour le deuxième compte
compte2 = CompteBancaire(numero_compte="789012", nom="Durand", prenom="Marie", solde=-200, decouvert=True)

# Virement du premier compte vers le deuxième compte
compte1.virement(compte_destinataire=compte2, montant=300)

# Affichage des soldes après le virement
compte1.afficher()
compte2.afficher()