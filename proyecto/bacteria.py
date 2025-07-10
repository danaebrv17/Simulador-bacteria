#id, raza
# energia
# resistente
#estado
#metodos alimentar(), dividirse(), mutar()y morir()

# Clase que representa una bacteria individual
class Bacteria:
    def __init__(self, id_bacteria, raza):
        # identificador unico de la bacteria
        self.id = id_bacteria

        # raza de la bacteria (por ejemplo: "A" o "B")
        self.raza = raza

        # energia actual de la bacteria
        self.energia = 5

        # si la bacteria es resistente a ataques o no
        self.resistente = False

        # si la bacteria esta viva o no
        self.viva = True

        self.recien_nacida = False
        self.fue_atacada = False
