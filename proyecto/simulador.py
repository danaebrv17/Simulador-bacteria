# Clase que conecta el simulador con la colonia
class Simulador:
    def __init__(self, colonia):
        self.colonia = colonia

    def avanzar_turno(self, consola=True):
        eventos = self.colonia.paso()
        if consola:
            print(f"Turno completado: {eventos['divisiones']} divisiones, {eventos['mutaciones']} mutaciones, {eventos['muertes']} muertes, {eventos['ataques']} ataques")
        return eventos
