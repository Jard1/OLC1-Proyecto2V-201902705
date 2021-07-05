from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break
from Analizador.Instrucciones.Return import Return
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.Instrucciones.Continue import Continue
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract



class Funcion(Instruccion):
    def __init__(self, fila, columna, nombre, instrucciones, parametros):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()

        self.instrucciones = instrucciones
        self.parametros = parametros
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):

        nuevaTabla = TablaSimbolos(table)

        for instruccion in self.instrucciones:

            value = instruccion.interpretar(tree,nuevaTabla)
            
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsole(value.toString())
            
            if isinstance(value, Break): 
                error = Excepcion("No se puede declarar un break fuera de un ciclo", "Semantico", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(error)
                tree.updateConsola(error.toString())
            if isinstance(value,Continue):
                error = Excepcion("No se puede declarar un continue fuera de un ciclo", "Semantico", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(error)
                tree.updateConsola(error.toString())

            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.result
        
        return None


    def getNodo(self):
        nodo = NodoASTabstract("Funcion")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoASTabstract("Conjunto Parametros")
        for param in self.parametros:
            parametro = NodoASTabstract("Parametro")
            parametro.agregarHijo(param["tipo"])
            parametro.agregarHijo(param["identificador"])
            parametros.agregarHijoNodo(parametro)
        nodo.agregarHijoNodo(parametros)

        instrucciones = NodoASTabstract("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo