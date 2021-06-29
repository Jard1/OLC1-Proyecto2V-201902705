from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break


class Funcion(Instruccion):
    def __init__(self, fila, columna, nombre, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()

        self.instrucciones = instrucciones
        self.tipo = None
    
    def interpretar(self, tree, table):

        nuevaTabla = TablaSimbolos(table)

        for instruccion in self.instrucciones:

            value = instruccion.interpretar(tree,nuevaTabla)
            
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
            
            if isinstance(value, Break): 
                error = Excepcion("No se puede declarar un break fuera de un ciclo", "Semantico", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(error)
                tree.updateConsola(error.toString())
        
        return None