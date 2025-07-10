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
fig, ax = plt.subplots(figsize=(6, 6))#crea figura y eje para graficar con matplotib
    cax = ax.matshow(grilla, cmap=cmap, vmin=0, vmax=5) #muestra la grilla como imagen de colores
        #creo leyenda personalizada
    leyenda = [
        Patch(facecolor=cmap(1/6), label="Viva"),
        Patch(facecolor=cmap(2/6), label="Muerta"),
        Patch(facecolor=cmap(3/6), label="Resistente"),
        Patch(facecolor=cmap(4/6), label="Hija"),
        Patch(facecolor=cmap(5/6), label="Atacada"),
    ]
    ax.legend(handles=leyenda, loc="upper right", bbox_to_anchor=(1.3, 1)) #agrega leyenda al grafico
    #rejilla visual para dividir las celdas
    ax.set_xticks(np.arange(0, ambiente.columnas, 1))
    ax.set_yticks(np.arange(0, ambiente.filas, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color="gray", linestyle="-", linewidth=0.5)
 for fila in range(ambiente.filas):
        for columna in range(ambiente.columnas):
            valor = grilla[fila, columna]
            if valor > 0:
                ax.text(columna, fila, int(valor), va="center", ha="center", color="white")

    plt.title("Grilla de bacterias - Eventos biologicos")
    plt.tight_layout()
    plt.show()
