
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

        if simbolo.getTipo() == TIPO.ENTERO:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo INT')

        elif simbolo.getTipo() == TIPO.DECIMAL:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo DOUBLE')

        elif simbolo.getTipo() == TIPO.CADENA:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo STRING')

        elif simbolo.getTipo() == TIPO.CHARACTER:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo CHAR')

        elif simbolo.getTipo() == TIPO.BOOLEANO:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo BOOL')

        elif simbolo.getTipo() == TIPO.NULO:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo NULL')

        elif simbolo.getTipo() == TIPO.ARREGLO:
            self.tipo = simbolo.getTipo()
            return tree.updateConsole('Tipo ARREGLO -> X')

        else:    
            return Excepcion("No se pudo determinar el tipo del valor ingresado","Semantico", self.fila, self.columna)
