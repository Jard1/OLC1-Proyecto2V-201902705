
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.Instrucciones.Funcion import Funcion

class TypeOf(Funcion): #hereda de funcion

    def __init__(self, fila, columna, nombre, parametros, instrucciones):
        
        self.fila = fila
        self.columna = columna
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeOf@") #para que sea imposible que exista una variable con ese nombre
        if simbolo == None : 
            return Excepcion("No se encontró el parámetro de TypeOf", "Semantico", self.fila, self.columna)

        
        tipoDeterminado = self.determinarTipo(simbolo.getTipo())

        if isinstance(tipoDeterminado, Excepcion):
            return tipoDeterminado

        if simbolo.getArreglo():
            self.tipo = simbolo.getTipo()
            return 'ARREGLO->'+tipoDeterminado
        return tipoDeterminado

    def determinarTipo(self, valor):
        if valor == TIPO.ENTERO:
            self.tipo = valor
            #return tree.updateConsole('Tipo INT')
            return 'INT'
        elif valor == TIPO.DECIMAL:
            self.tipo = valor
            return 'DOUBLE'

        elif valor == TIPO.CADENA:
            self.tipo = valor
            return 'STRING'

        elif valor == TIPO.CHARACTER:
            self.tipo = valor
            return 'CHAR'

        elif valor == TIPO.BOOLEANO:
            self.tipo = valor
            return 'BOOL'

        elif valor == TIPO.NULO:
            self.tipo = valor
            return 'NULL'

        else:    
            return Excepcion("No se pudo determinar el tipo del valor ingresado","Semantico", self.fila, self.columna)