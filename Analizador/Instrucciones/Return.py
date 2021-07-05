from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Return(Instruccion):
    
    def __init__(self, fila, columna, expresion):
        
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        
        self.tipo = None
        self.result = None

    def interpretar(self, tree, table):

        valor = self.expresion.interpretar(tree, table)
        if isinstance(valor, Excepcion): 
            return valor

        self.tipo = self.expresion.tipo
        self.result = valor
        return self #para poder acceder a todos los atributos


    def getNodo(self):
        nodo = NodoASTabstract("Return")

        nodo.agregarHijoNodo(self.expresion.getNodo())

        return nodo