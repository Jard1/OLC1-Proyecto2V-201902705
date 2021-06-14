from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion

class Identificador(Instruccion):
    def __init__(self, fila, columna, identificador):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = None #inicialmente no sabemos el tipo

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower()) #Buscamos la variable

        if simbolo == None:
            #no enocnotro la variable en la tabla de simbolos
            return Excepcion("La Variable " + self.identificador + " no ha sido declarada","Semantico", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        
        return simbolo.getValor()