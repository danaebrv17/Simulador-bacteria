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
 # Metodo para dividirse en una hija si tiene energia suficiente
    def dividirse(self, nuevo_id):
        if self.viva and self.energia >= 20: #para dividirse tendra 20 o mas de energia
            energia_hija = self.energia // 2
            self.energia = energia_hija #creo onjeto bacteria nuevo
            hija = Bacteria(nuevo_id, self.raza, energia_hija, self.resistente)
            hija.recien_nacida = True
            return hija
        return None

    # Metodo para mutar con cierta probabilidad
    def mutar(self, probabilidad=0.1):
        import random 
        if self.viva and not self.resistente: #mutara solo si esta viva y no es resistente
            if random.random() < probabilidad: #si el numero es menor a 0.1 se vuelve resistente
                self.resistente = True
