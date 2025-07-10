# Clase que administrara la colonia de bacterias en el ambiente
#bacteria como lista de objetos
#ambiente como instancia de clase ambiente
#metodo paso(), reporte estado(), exportar csv()
import random
import csv
from bacteria import Bacteria

# Clase que administra la colonia de bacterias en el ambiente
class Colonia:
    def __init__(self, ambiente): # colonia contiene al ambiente
        self.ambiente = ambiente
        self.bacterias = []
        self.contador_id = 1
        
 # Metodo principal que ejecuta un turno de simulacion
    def paso(self):
        nuevas_bacterias = [] #lista psrs guardar a bacterias hijas
        eventos = {
            "divisiones": 0,
            "mutaciones": 0,
            "muertes": 0,
            "ataques": 0
        }
        #recorro la grilla
        for fila in range(self.ambiente.filas):
            for columna in range(self.ambiente.columnas):
                bacteria = self.ambiente.grilla[fila][columna] #accedo a celda de la grilla
                if bacteria is not None and bacteria.viva: #si hay bacteria viva se ejecutan los eventos 

                    # Alimentar
                    # Mutar
                    # Reproducirse
                    # Atacar
                    
        return eventos   
