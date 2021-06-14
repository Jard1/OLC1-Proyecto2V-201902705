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
            self.determinarTipo(value)
            if isinstance(value, Excepcion): 
                return value #Si es un error, lo retornamos

            simbolo = Simbolo(self.fila, self.columna, str(self.identificador), value, self.tipo )

            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): 
                return result
            return None #la declaracion fue correcta

    
    def determinarTipo(self,value):
        
        if value == "null":
            print("valor nulo")
            self.tipo = TIPO.NULO
        elif type(value) == int:
            self.tipo = TIPO.ENTERO
        elif type(value) == float:
            self.tipo = TIPO.DECIMAL
        elif type(value) == bool:
            self.tipo = TIPO.BOOLEANO
        elif type(value) == str:
            if len(value) == 1:
                self.tipo = TIPO.CHARACTER
            else:
                self.tipo = TIPO.CADENA

        return Excepcion("Semantico", "Tipo de dato no definido", self.fila, self.columna)



