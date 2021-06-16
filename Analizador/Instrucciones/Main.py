from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO
from TablaSimbolos.simbolo import Simbolo
from TablaSimbolos.tablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class Main(Instruccion):

    def __init__(self,fila, columna, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.instrucciones = instrucciones 

    def interpretar(self, tree, table):
        #creamos un nuevo entorno
        nuevaTabla = TablaSimbolos(table)
        # realizar las instrucciones deseadas, que estan guardadas en el ast
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(tree,nuevaTabla)
        if isinstance(value, Excepcion) :
            tree.getExcepciones().append(value)
            tree.updateConsole(value.toString())
        if isinstance(value, Break) :
            error =  Excepcion("No se puede declarar un break fuera de un ciclo","Semantico", instruccion.fila,instruccion.columna)
            tree.getExcepciones().append(error)
            tree.updateConsole(error.toString())
            #break