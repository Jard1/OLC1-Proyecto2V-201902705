from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO
from TablaSimbolos.tablaSimbolos import TablaSimbolos

class If(Instruccion):

    def __init__(self, fila, columna, expresionCondicion, instruccionesIf, instruccionesElse, elseIf):

        self.fila = fila
        self.columna = columna
        self.expresionCondicion = expresionCondicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = elseIf

    def interpretar(self, tree, table):
        condicion = self.expresionCondicion.interpretar(tree, table) #interpretamos la condicion

        if isinstance(condicion, Excepcion): 
            #si hay error, lo retornamos
            return condicion

        if self.expresionCondicion.tipo == TIPO.BOOLEANO:
            #---------------------------------------IF = TRUE---------------------------------------
            if bool(condicion) == True:
                #Instrucciones por hacer si es verdadera la condicion

                TablaIF = TablaSimbolos(table)  #nueva tabla de simbolos, es decir un nuevo ambito

                for inst in self.instruccionesIf:
                    #ejecutamos todas las instrucciones dentro del if
                    result = inst.interpretar(tree, TablaIF)

                    if isinstance(result, Excepcion) :
                        tree.getExcepciones().append(result)
                        tree.updateConsole(result.toString())

            #-------------------------------------IF = False--------------------------------------------
            else:

                if self.instruccionesElse != None:
                    #Si vienen instrucciones en el else
                    #creamos un nuevo entorno
                    TablaIfElse = TablaSimbolos(table)

                    for instruccion in self.instruccionesElse:
                        #ejecutamos cada instruccion
                        result = instruccion.interpretar(tree, TablaIfElse) 
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString()) 
                elif self.elseIf != None:
                    #llamada recursiva al metodo interpretar nuevamente
                    result = self.elseIf.interpretar(tree, table)
                    if isinstance(result, Excepcion): 
                        return result

        else:
            return Excepcion("La expresion ingresada como condicion tiene que ser booleana","Semantico", self.fila, self.columna)
    

def stringToBool(self,val):
    #pasa todo a minustulas y luego mira si la palabra es true
    return val.lower() in ("true")