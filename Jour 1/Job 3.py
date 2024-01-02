class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)

# Création d'une instance de la classe Operation
operation_instance = Operation(12, 3)

# Impression des valeurs des attributs "nombre1" et "nombre2"
print("Le nombre1 est", operation_instance.nombre1)
print("Le nombre2 est", operation_instance.nombre2)

# Appel de la méthode addition et affichage du résultat
operation_instance.addition()