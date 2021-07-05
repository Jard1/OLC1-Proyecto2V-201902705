
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.Instrucciones.Funcion import Funcion
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Length(Funcion): #hereda de funcion

    def __init__(self, fila, columna, nombre, parametros, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("length@") #para que sea imposible que exista una variable con ese nombre
        if simbolo == None : 
            return Excepcion("No se encontró el parámetro de Length", "Semantico", self.fila, self.columna)

        if simbolo.getTipo() == TIPO.ARREGLO or simbolo.getTipo() == TIPO.CADENA:
            
            self.tipo = simbolo.getTipo()
            return len(simbolo.getValor())
        elif simbolo.getArreglo():
            self.tipo = simbolo.getTipo()
            return len(simbolo.getValor())
        else:    
            return Excepcion("La funcion Length solo acepta cadenas o vectores linealizados","Semantico", self.fila, self.columna)

    #def getNodo(self):
     #   nodo = NodoASTabstract("Length")
      #  nodo.agregarHijo(str(self.nombre))
        
       # return nodo