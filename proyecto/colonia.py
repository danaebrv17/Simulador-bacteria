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
                    nutrientes = self.ambiente.nutrientes[fila][columna]
                    consumido = bacteria.alimentar(nutrientes)
                    self.ambiente.nutrientes[fila][columna] = max(nutrientes - consumido, 0)

                    # Mutar
                    antes = bacteria.resistente # si la bacteria era resistente antes de mutar
                    bacteria.mutar() #llamo a metodo mutar en bacteria
                    if not antes and bacteria.resistente: #verifico que no era resistente 
                        eventos["mutaciones"] += 1

                    # Reproducirse
                    hija = bacteria.dividirse(self.contador_id) #llamo a metodo div en bacteria y si tiene energia devuelve hija
                    if hija:
                        vecinos_libres = self.ambiente.obtener_vecinos_libres(fila, columna) #veo que celdas al rededor estan vacias
                        if vecinos_libres:
                            nueva_fila, nueva_columna = random.choice(vecinos_libres) #elijo una de esas celdas al azar 
                            self.ambiente.grilla[nueva_fila][nueva_columna] = hija #coloco a bacteria hija
                            nuevas_bacterias.append(hija) #agredo a lista de bacterias nuevas
                            self.contador_id += 1 
                            eventos["divisiones"] += 1

                    # Atacar
                    vecinos_ocupados = self.ambiente.obtener_vecinos_ocupados(fila, columna)#radio de ataque
                    if vecinos_ocupados: #verifico si una bacteria vecina puede ser atacada
                        objetivo_fila, objetivo_columna = random.choice(vecinos_ocupados) #elijo al azar una de ellas
                        objetivo = self.ambiente.grilla[objetivo_fila][objetivo_columna]
                        if objetivo is not None and objetivo.viva and objetivo.id != bacteria.id: #existe? esta viva? no se ataque sola
                            objetivo.recibir_ataque() #mata bacteria si no es resistente
                            if not objetivo.viva:
                                eventos["muertes"] += 1
                            eventos["ataques"] += 1

        self.bacterias.extend(nuevas_bacterias)           
        return eventos 
        # Reportar estado al usuario
    def reporte_estado(self):
        total = 0
        vivas = 0
        resistentes = 0
        muertas = 0
        for fila in self.ambiente.grilla: #busco en las filas 
            for celda in fila: #busco los elementos en cada fila
                if celda is not None: # analiso si la celda tiene bacteria
                    total += 1
                    if celda.viva:
                        vivas += 1
                        if celda.resistente:
                            resistentes += 1
                    else:
                        muertas += 1
        print(f"Total: {total}, Vivas: {vivas}, Muertas: {muertas}, Resistentes: {resistentes}")
