
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.Instrucciones.Funcion import Funcion
import math

class Truncate(Funcion): #hereda de funcion

    def __init__(self, fila, columna, nombre, parametros, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("truncate@") #para que sea imposible que exista una variable con ese nombre
        if simbolo == None : 
            return Excepcion("No se encontró el parámetro de Truncate", "Semantico", self.fila, self.columna)

        if simbolo.getTipo() == TIPO.ENTERO or simbolo.getTipo() == TIPO.DECIMAL:
            
            self.tipo = simbolo.getTipo()
            return math.trunc(simbolo.getValor())

        else:    
            return Excepcion("La funcion Truncate solo acepta enteros o decimales","Semantico", self.fila, self.columna)
