from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.Instrucciones.Break import Break
from Analizador.Instrucciones.Continue import Continue
from Analizador.Instrucciones.Return import Return
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract


class Case (Instruccion):
    def __init__(self, fila, columna, expresionPorValidar, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.expresionPorValidar = expresionPorValidar
        self.instrucciones = instrucciones

    def interpretar(self, tree, table):

        nuevaTabla = TablaSimbolos(table)       
        for instruccion in self.instrucciones:

            result = instruccion.interpretar(tree, nuevaTabla)
            if isinstance(result, Excepcion):
                tree.getExcepciones().append(result)
            if isinstance(result, Break): 
                return result
            if isinstance(result,Continue):
                break
            if isinstance(result, Return):
                return result
            

    def getNodo(self):
        nodo = NodoASTabstract("Case")

        instrucciones = NodoASTabstract("Instrucciones - Case")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo