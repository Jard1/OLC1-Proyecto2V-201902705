from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Continue(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        #return self #con esto debolvemos la instancia del Continue para que otras clases puedan saber que es un break
        return self

    def getNodo(self):
        nodo = NodoASTabstract("Continue")
        return nodo