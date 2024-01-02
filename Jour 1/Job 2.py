class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Création d'une instance de la classe Operation avec les valeurs spécifiées
operation_instance = Operation(12, 3)

# Impression des valeurs des attributs
print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")