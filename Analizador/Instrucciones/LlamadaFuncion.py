from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break


class LlamadaFuncion(Instruccion):
    def __init__(self, fila, columna, nombre ):

        self.fila = fila
        self.columna = columna
        self.nombre = nombre
    
    def interpretar(self, tree, table):

        funcion = tree.getFuncion(self.nombre.lower()) 
        
        if funcion == None:
            return Excepcion("La funcion " + self.nombre+" No ha sido declarada","Semantico", self.fila, self.columna)

        #parametros

        value = funcion.interpretar(tree, table)
        if isinstance(value, Excepcion): 
            return value
        self.tipo = funcion.tipo

        return value