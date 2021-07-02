
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.Instrucciones.Funcion import Funcion

class ToLower(Funcion): #hereda de funcion

    def __init__(self, fila, columna, nombre, parametros, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("toLower@Parametro1") #para que sea imposible que exista una variable con ese nombre
        if simbolo == None : 
            return Excepcion("No se encontró el parámetro de ToUpper", "Semantico", self.fila, self.columna)

        if simbolo.getTipo() == TIPO.CADENA:
            
            self.tipo = simbolo.getTipo()
            return simbolo.getValor().lower()

        else:    
            return Excepcion("Semantico", "La funcion ToUpper solo acepta cadenas", self.fila, self.columna)
