#sera una grilla 10 x 10
#debe tener nutrientes
#metodos actualizar nutrientes(), aplicar ambiente()
import random

# Clase que representa el entorno de la simulacion
class Ambiente:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas

        # Crear grilla vacia con None
        self.grilla = []
        for fila in range(filas):
            fila_lista = []
            for columna in range(columnas):
                fila_lista.append(None)
            self.grilla.append(fila_lista)

        # Crear matriz de nutrientes aleatorios
        self.nutrientes = []
        for fila in range(filas):
            fila_nutrientes = []
            for columna in range(columnas):
                fila_nutrientes.append(random.randint(1, 5))
            self.nutrientes.append(fila_nutrientes)
