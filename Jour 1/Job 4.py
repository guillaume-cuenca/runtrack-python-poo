class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return "Je suis {} {}".format(self.prenom, self.nom)

# Instanciation de plusieurs personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Appel de la méthode SePresenter pour chaque personne
resultat1 = personne1.SePresenter()
resultat2 = personne2.SePresenter()

# Affichage des résultats
print(resultat1)
print(resultat2)