# Clase que conecta el simulador con la colonias
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Visualiza la grilla del ambiente con distintos colores por tipo de bacteria
def visualizar_grilla(ambiente):
    grilla = np.zeros((ambiente.filas, ambiente.columnas)) #creo matriz 2d con 0 con el tamaño de ambiente

    for fila in range(ambiente.filas):#reccorro cada celda 
        for columna in range(ambiente.columnas):
            celda = ambiente.grilla[fila][columna]
            if celda is not None: 
                if celda.fue_atacada:
                    grilla[fila, columna] = 5
                elif not celda.viva:
                    grilla[fila, columna] = 2
                elif celda.recien_nacida:
                    grilla[fila, columna] = 4
                elif celda.resistente:
                    grilla[fila, columna] = 3
                else:
                    grilla[fila, columna] = 1

    cmap = plt.cm.get_cmap("Set1", 6) # selecciono paleta de 6 colores
