from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.Instrucciones.Break import Break
from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.Instrucciones.Continue import Continue
from Analizador.Instrucciones.Return import Return
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Switch(Instruccion):

    def __init__(self, fila, columna, expresionPorEvaluar, listaCases, default):

        self.fila = fila
        self.columna = columna
        self.expresionPorEvaluar = expresionPorEvaluar
        self.listaCases = listaCases
        self.default = default

    def interpretar(self, tree, table):

        condicion = self.expresionPorEvaluar.interpretar(tree, table)
        if isinstance(condicion, Excepcion): 
            return condicion


        if self.listaCases != None:

            for case in self.listaCases:

                valorComparacion = case.expresionPorValidar.interpretar(tree, table)
                
                if isinstance(valorComparacion, Excepcion):
                    tree.getExcepciones().append(valorComparacion)
                else:
                    if valorComparacion == condicion: 

                        result = case.interpretar(tree, table) 
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                        if isinstance(result, Break): 
                            return None 
                        if isinstance(result,Continue):
                            break
                        if isinstance(result, Return):
                            return result
            
        #-------------------------Instrucciones del default-------------------------------
        if self.default != None:
            variabledefault = self.default.interpretar(tree, table)
            if isinstance(variabledefault, Excepcion) :
                tree.getExcepciones().append(variabledefault)
                #tree.updateConsola(variabledefault.toString())
            if isinstance(variabledefault, Break): 
                return None


def getNodo(self):
    nodo = NodoASTabstract("Switch")

    nodoExp = NodoASTabstract("Expresion")
    nodoExp.agregarHijoNodo(self.expresionPorEvaluar.getNodo())
    nodo.agregarHijoNodo(nodoExp)

    if self.listaCases != None:
        instrucciones = NodoASTabstract("Instrucciones - Case")
        for cases in self.listaCases:
            instrucciones.agregarHijoNodo(cases.getNodo())
        nodo.agregarHijoNodo(instrucciones)
    

    if self.default != None:
        instruccionesDefault = NodoASTabstract("Instrucciones - Default")
        for instr in self.instruccionesElse:
            instruccionesDefault.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instruccionesDefault) 

    return nodo