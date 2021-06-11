from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO

class Imprimir(Instruccion): #hacemos la herencia

    #constructor
    def __init__(self, fila, columna, expresion):
        
        self.fila = fila
        self.columna = columna
        
        self.expresion = expresion #esto depende de la gramatica

    def interpretar(self, tree, table):
        #esto es porque el expresion es una instruccion y retorna cualquier valor
        value = self.expresion.interpretar(tree, table)

        #verifica si el valor tiene una instancia de error
        if isinstance(value, Excepcion) :
            return value

        #validaciones semanticas para no dejar imprimir un arreglo completo
        if self.expresion.tipo == TIPO.ARREGLO:
            return Excepcion("No se puede imprimir un arreglo","Semantico", self.fila, self.columna)
        
        tree.updateConsole(value) 
