from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break
from Analizador.Instrucciones.Continue import Continue
from Analizador.Instrucciones.Asignacion import Asignacion
from Analizador.Instrucciones.Return import Return
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract


class For(Instruccion):

    def __init__(self, fila, columna, inicializacion, Expresioncondicion, actualizacion , instrucciones ):
        
        self.fila = fila
        self.columna = columna
        self.inicializacion = inicializacion
        self.Expresioncondicion = Expresioncondicion
        self.actualizacion = actualizacion
        self.instrucciones = instrucciones

    def interpretar(self, tree, table):

        if isinstance(self.inicializacion, Asignacion): 

            iniciarVariable = self.inicializacion.interpretar(tree,table)

            if isinstance(iniciarVariable, Excepcion): 
                return iniciarVariable
        
        tablaFor = TablaSimbolos(table)
        declaracion = self.inicializacion.interpretar(tree, tablaFor)

        if isinstance(declaracion, Excepcion): 
            return declaracion

        while True:
            
            condicion = self.Expresioncondicion.interpretar(tree, tablaFor)
            if isinstance(condicion, Excepcion): 
                return condicion

            #la condicion tiene que ser booleana
            if self.Expresioncondicion.tipo == TIPO.BOOLEANO:
                
                # Si la condicion es verdadera ingresa al bucle, de lo contrario sale con un break
                if bool(condicion) == True:  
                    #creamos un nuevo entorno
                    nuevaTabla = TablaSimbolos(tablaFor)
                    
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
                        if isinstance(result, Return):
                            return result
                            
                    actualizar = self.actualizacion.interpretar(tree, tablaFor)
                    if isinstance(actualizar, Excepcion): 
                        return actualizar

                else:
                    break
            else:
                return Excepcion("La expresion ingresada como condicion tiene que ser booleana","Semantico", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoASTabstract("For")

        instrucciones = NodoASTabstract("Instrucciones - For")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo