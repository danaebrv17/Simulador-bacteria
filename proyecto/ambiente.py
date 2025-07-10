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
            
 # Metodo que entrega vecinos libres de una celda dada
    def obtener_vecinos_libres(self, fila, columna):
        vecinos = []
        for delta_fila in [-1, 0, 1]:
            for delta_columna in [-1, 0, 1]:
                if delta_fila == 0 and delta_columna == 0:
                    continue
                nueva_fila = fila + delta_fila
                nueva_columna = columna + delta_columna
                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                    if self.grilla[nueva_fila][nueva_columna] is None:
                        vecinos.append((nueva_fila, nueva_columna))
        return vecinos
 # Metodo que entrega vecinos ocupados (para posibles ataques)
    def obtener_vecinos_ocupados(self, fila, columna):
        vecinos = []
        for delta_fila in [-1, 0, 1]:
            for delta_columna in [-1, 0, 1]:
                if delta_fila == 0 and delta_columna == 0:
                    continue
                nueva_fila = fila + delta_fila
                nueva_columna = columna + delta_columna
                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                    if self.grilla[nueva_fila][nueva_columna] is not None:
                        vecinos.append((nueva_fila, nueva_columna))
        return vecinos
