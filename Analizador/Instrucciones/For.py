from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break
from Analizador.Instrucciones.Continue import Continue


class For(Instruccion):

    def __init__(self, fila, columna, inicializacion, Expresioncondicion, actualizacion , instrucciones ):
        
        self.fila = fila
        self.columna = columna
        self.inicializacion = inicializacion
        self.Expresioncondicion = Expresioncondicion
        self.actualizacion = actualizacion
        self.instrucciones = instrucciones

    def interpretar(self, tree, table):

        iniciarVariable = self.inicializacion.interpretar(tree,table)
        
        if isinstance(iniciarVariable, Excepcion): 
            return iniciarVariable
        while True:
            
            condicion = self.Expresioncondicion.interpretar(tree, table)

            if isinstance(condicion, Excepcion): 
                return condicion

            #la condicion tiene que ser booleana
            if self.Expresioncondicion.tipo == TIPO.BOOLEANO:
                
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
                        if isinstance(result,Continue):
                            break
                        
                    actualizar = self.actualizacion.interpretar(tree, table)
                    if isinstance(actualizar, Excepcion): 
                        return actualizar


                else:
                    break
            else:
                return Excepcion("La expresion ingresada como condicion tiene que ser booleana","Semantico", self.fila, self.columna)