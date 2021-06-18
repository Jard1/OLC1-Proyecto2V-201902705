from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.simbolo import Simbolo

class Asignacion(Instruccion):

    def __init__(self, fila, columna , identificador, expresion ):
        
        self.fila = fila
        self.columna = columna

        self.identificador = identificador
        self.expresion = expresion

    def interpretar(self, tree, table):
        
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Excepcion): 
            return value

        simbolo = Simbolo(self.fila, self.columna, self.identificador, value, self.expresion.tipo)

        result = table.actualizarTabla(simbolo)

        if isinstance(result, Excepcion): 
            return result
        
        return None