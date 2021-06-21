from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.Instrucciones.Break import Break
from Analizador.TablaSimbolos.instruccionAbstract import Instruccion

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
            
        #-------------------------Instrucciones del default-------------------------------
        if self.default != None:
            variabledefault = self.default.interpretar(tree, table)
            if isinstance(variabledefault, Excepcion) :
                tree.getExcepciones().append(variabledefault)
                #tree.updateConsola(variabledefault.toString())
            if isinstance(variabledefault, Break): 
                return None