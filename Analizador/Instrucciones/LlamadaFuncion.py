from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tablaSimbolos import TablaSimbolos
from Analizador.Instrucciones.Break import Break
from Analizador.TablaSimbolos.simbolo import Simbolo
from Analizador.Expresiones.Identificador import Identificador
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract


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

        nuevaTabla = TablaSimbolos(tree.getTSGlobal()) #se usa la tabla global para soportar la recursividad

        #-------------------------------------------------parametros--------------------------------------------------------
        #verificamos si es la cantidad de parametros esperada
        if len(funcion.parametros) == len(self.parametros):
            cont=0
            #recorremos los parametros
            for expresion in self.parametros:
                
                valorExpresion = expresion.interpretar(tree, table)
                #si es un error
                if isinstance(valorExpresion, Excepcion): 
                    return valorExpresion
                
                #casos especificos para las funciones nativas, la verificacion de tipos se hace en cada funcion nativa
                if funcion.parametros[cont]['identificador'].lower() == 'truncate@' or funcion.parametros[cont]['identificador'].lower() == 'round@' or funcion.parametros[cont]['identificador'].lower() == 'typeof@' or funcion.parametros[cont]['identificador'].lower() == 'length@':
                    funcion.parametros[cont]["tipo"] = expresion.tipo
                
                #verificamos que los tipos sean los mismos
                if funcion.parametros[cont]["tipo"] == expresion.tipo:

                    #------------registramos los parametros como nuevas variables-------------
                    if isinstance (expresion, Identificador):
                        if expresion.getArreglo():
                            simbolo = Simbolo(self.fila, self.columna, str(funcion.parametros[cont]['identificador']).lower(), valorExpresion , funcion.parametros[cont]['tipo'],True)
                        else:
                            simbolo = Simbolo(self.fila, self.columna, str(funcion.parametros[cont]['identificador']).lower(), valorExpresion , funcion.parametros[cont]['tipo'])
                    else:
                        simbolo = Simbolo(self.fila, self.columna, str(funcion.parametros[cont]['identificador']).lower(), valorExpresion , funcion.parametros[cont]['tipo'])
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

    def getNodo(self):
        nodo = NodoASTabstract("Llamada - Funcion")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoASTabstract("Parametros")
        for param in self.parametros:
            parametros.agregarHijoNodo(param.getNodo())
        nodo.agregarHijoNodo(parametros)
        return nodo