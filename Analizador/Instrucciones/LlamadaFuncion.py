from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break
from Analizador.TablaSimbolos.simbolo import Simbolo


class LlamadaFuncion(Instruccion):
    def __init__(self, fila, columna, nombre, parametros ):

        self.fila = fila
        self.columna = columna
        self.nombre = nombre
        self.parametros = parametros
    
    #falta los arreglos
    def interpretar(self, tree, table):

        funcion = tree.getFuncion(self.nombre.lower()) 
        
        if funcion == None:
            return Excepcion("La funcion " + self.nombre+" No ha sido declarada","Semantico", self.fila, self.columna)

        nuevaTabla = TablaSimbolos(table)
        #-------------------------------------------------parametros--------------------------------------------------------
        #verificamos si es la cantidad de parametros esperada
        if len(funcion.parametros) == len(self.parametros):
            cont=0
            #recorremos los parametros
            for expresion in self.parametros:
                
                valorExpresion = expresion.interpretar(tree, nuevaTabla)
                #si es un error
                if isinstance(valorExpresion, Excepcion): 
                    return valorExpresion
                
                #verificamos que los tipos sean los mismos
                if funcion.parametros[cont]["tipo"] == expresion.tipo:

                    #------------registramos los parametros como nuevas variables-------------
                    simbolo = Simbolo(self.fila, self.columna, str(funcion.parametros[cont]['identificador']), valorExpresion , funcion.parametros[cont]['tipo'])
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion): 
                        return resultTabla

                else:
                    return Excepcion("El tipo de dato ingresado no coincide con el del parametro", "Semantico", self.fila, self.columna)
                cont += 1
            
        else: 
            return Excepcion("No se esta ingresando la cantidad de parametros esperados", "Semantico", self.fila, self.columna)

        value = funcion.interpretar(tree, nuevaTabla)
        if isinstance(value, Excepcion): 
            return value
        self.tipo = funcion.tipo

        return value