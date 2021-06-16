from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO
from TablaSimbolos.simbolo import Simbolo

class Declaracion(Instruccion):

    def __init__(self,fila, columna, identificador,expresion=None):
        
        self.identificador = identificador 
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.expresion == None:
            #-----------No viene una expresion-----------
            value = "null"
            self.tipo = TIPO.NULO
            simbolo = Simbolo(self.fila, self.columna, str(self.identificador), value, self.tipo)
            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): 
                return result
            return None 

        else:
            value = self.expresion.interpretar(tree, table) # Valor por asignar
            self.tipo = self.expresion.tipo
            if isinstance(value, Excepcion): 
                return value #Si es un error, lo retornamos

            simbolo = Simbolo(self.fila, self.columna, str(self.identificador), value, self.tipo )

            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): 
                return result
            return None #la declaracion fue correcta

    
