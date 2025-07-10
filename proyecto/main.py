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
        
       def agregar_bacterias_iniciales(self, cantidad):
        contador = 0
        while contador < cantidad:
            fila = random.randint(0, self.ambiente.filas - 1)
            columna = random.randint(0, self.ambiente.columnas - 1)#busco posiciones vacias
            if self.ambiente.grilla[fila][columna] is None: #al encontar una vacia coloca bacteria ahi 
                nueva = Bacteria(self.colonia.contador_id, "A") #creo bacteria con su id y raza
                self.ambiente.grilla[fila][columna] = nueva # se agrega en una celda vacia de la grilla
                self.colonia.bacterias.append(nueva) # tambien se agrega a la lista de bacterias de la colonia 
                self.colonia.contador_id += 1 #incremento para nuevo id 
                contador += 1

def avanzar_turno(self, widget):
        if self.turno < self.turno_maximo:
            eventos = self.simulador.avanzar_turno(consola=False) #llamo al simulador para ejecutar tuno
            linea = f"Turno {self.turno + 1}: {eventos['divisiones']} divisiones, {eventos['mutaciones']} mutaciones, {eventos['muertes']} muertes, {eventos['ataques']} ataques\n"
            self.mostrar_texto(linea)
            visualizar_grilla(self.ambiente)#muestra la grilla actualizada con los nuevos estados
            self.turno += 1
            self.reiniciar_flags_visuales()#limpio los flags
        else:
            self.mostrar_texto("simulacion completada.\n")
            self.colonia.exportar_csv() #guado el reporte csv
            self.boton_turno.set_sensitive(False)#desactivo el boton avanzar turno
def mostrar_texto(self, texto):
        fin = self.texto_eventos.get_end_iter()
        self.texto_eventos.insert(fin, texto)

    def reiniciar_flags_visuales(self):
        for fila in self.ambiente.grilla: #recorro la grilla y reinicnia los flags para mostar eventos actuales
            for celda in fila:
                if celda is not None:
                    celda.recien_nacida = False
                    celda.fue_atacada = False

class Aplicacion(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.simulador.bacterias")
    def do_activate(self):
        ventana = VentanaSimulacion(self)
        ventana.present()

def main():
    app = Aplicacion()
    app.run()

if __name__ == "__main__":
    main()
