class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                return f"Tâche '{titre}' supprimée avec succès."
        return f"Tâche '{titre}' non trouvée."

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                return f"Tâche '{titre}' marquée comme terminée."
        return f"Tâche '{titre}' non trouvée."

    def afficherListe(self):
        return [f"{tache.titre}: {tache.description} - Statut: {tache.statut}" for tache in self.taches]

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# Exemple d'utilisation
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5", "À faire")
tache3 = Tache("Faire du sport", "Jogging de 30 minutes")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste de toutes les tâches:")
print(liste_taches.afficherListe())

# Supprimer une tache
print("\nSupprimer une tâche:")
print(liste_taches.supprimerTache("Faire les courses"))
print(liste_taches.afficherListe())

# Changer le statut d'une tache
print("\nChanger le statut d'une tâche:")
print(liste_taches.marquerCommeFinie("Réviser pour l'examen"))
print(liste_taches.afficherListe())

# Afficher les tâches à faire
print("\nTâches à faire:")
taches_a_faire = liste_taches.filterListe("À faire")
print([f"{tache.titre}: {tache.description}" for tache in taches_a_faire])