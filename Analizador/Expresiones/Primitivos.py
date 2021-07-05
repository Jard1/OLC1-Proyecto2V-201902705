from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Primitivos(Instruccion): #hacemos la herencia

    #constructor
    def __init__(self, fila, columna, tipo, valor):
        
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor

    def interpretar(self, tree, table):
        return self.valor

    def getNodo(self):
        nodo = NodoASTabstract("Primitivo")
        nodo.agregarHijo(str(self.valor))
        return nodo