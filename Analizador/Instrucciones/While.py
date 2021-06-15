from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO
from TablaSimbolos.tablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class While(Instruccion):

    def __init__(self, fila, columna, condicion, instrucciones ):
        self.fila = fila
        self.columna = columna
        self.condicion = condicion
        self.instrucciones = instrucciones

    def interpretar(self, tree, table):
        
        while True:
            
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): 
                return condicion

            #la condicion tiene que ser booleana
            if self.condicion.tipo == TIPO.BOOLEANO:
                # Si la condicion es verdadera ingresa al bucle, de lo contrario sale con un break
                if bool(condicion) == True:  
                    #creamos un nuevo entorno
                    nuevaTabla = TablaSimbolos(table)
                    
                    #ejecutamos cada instruccion que venga dentro del while
                    for instruccion in self.instrucciones:
                    
                        result = instruccion.interpretar(tree, nuevaTabla) #ejecutamos la instruccion
                        if isinstance(result, Excepcion):
                            #si hay un error , se muestra en consola
                            tree.getExcepciones().append(result)
                            tree.updateConsole(result.toString())
                        
                        if isinstance(result, Break): 
                            #Retorna none para salirse del bucle
                            return None
                else:
                    break
            else:
                return Excepcion("La expresion ingresada como condicion tiene que ser booleana","Semantico", self.fila, self.columna)