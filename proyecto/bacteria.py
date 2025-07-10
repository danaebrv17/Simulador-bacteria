#id, raza
# energia
# resistente
#estado
#metodos alimentar(), dividirse(), mutar()y morir()

# Clase que representa una bacteria individual
class Bacteria:
    def __init__(self, id_bacteria, raza):
        self.id = id_bacteria              # id unico
        self.raza = raza                   #raza
        self.energia = energia             # nivel de energia
        self.resistente = resistente       # Si es resistente a ataques o no
        self.viva = True                   # estado de vida
        self.recien_nacida = False         # para marcar que es hija
        self.fue_atacada = False           # para marcar que fue atacada
# Metodo para alimentarse con nutrientes disponibles
    def alimentar(self, nutrientes_disponibles):
        if self.viva:
            energia_ganada = min(nutrientes_disponibles, 5)
            self.energia += energia_ganada
            return energia_ganada
        return 0

    # Metodo para morir (por ataque o falta de energia)
    def morir(self):
        self.viva = False
        self.energia = 0
