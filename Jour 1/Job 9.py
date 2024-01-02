class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        print(f"Nom: {self.nom}, Prix HT: {self.prixHT} EUR, TVA: {self.TVA}%")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Produit A", 50, 20)
produit2 = Produit("Produit B", 30, 10)
produit3 = Produit("Produit C", 80, 15)

# Affichage des informations initiales
produit1.afficher()
produit2.afficher()
produit3.afficher()

# Calcul des prix TTC
prixTTC_produit1 = produit1.CalculerPrixTTC()
prixTTC_produit2 = produit2.CalculerPrixTTC()
prixTTC_produit3 = produit3.CalculerPrixTTC()

# Affichage des prix TTC
print(f"Prix TTC du {produit1.getNom()}: {prixTTC_produit1} EUR")
print(f"Prix TTC du {produit2.getNom()}: {prixTTC_produit2} EUR")
print(f"Prix TTC du {produit3.getNom()}: {prixTTC_produit3} EUR")

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouveau Produit A")
produit1.modifierPrix(60)

produit2.modifierNom("Nouveau Produit B")
produit2.modifierPrix(35)

produit3.modifierNom("Nouveau Produit C")
produit3.modifierPrix(90)

# Affichage des nouvelles informations
produit1.afficher()
produit2.afficher()
produit3.afficher()