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
      
