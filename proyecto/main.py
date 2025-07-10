#crear bacteria , ambiente y colonia
from ambiente import Ambiente
from bacteria import Bacteria
from colonia import Colonia
from simulador import Simulador
from visualizacion import visualizar_grilla

import gi
import random
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class VentanaSimulacion(Gtk.ApplicationWindow): #ventana GTK donde usuario vera simulacion 
    def __init__(self, app): # constructor objeto ventana
        super().__init__(application=app)
        self.set_title("Simulador de Bacterias")
        self.set_default_size(600, 500)

        self.ambiente = Ambiente(10, 10)
        self.colonia = Colonia(self.ambiente) #colonia guarda el ambiente
        self.simulador = Simulador(self.colonia) #simulador contendra colonia 
        self.turno = 0
        self.turno_maximo = 5
        nueva = Bacteria(self.colonia.contador_id, "A") #creo bacteria con su id y raza
