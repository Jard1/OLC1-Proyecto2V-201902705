from Analizador.TablaSimbolos.instruccionAbstract import Instruccion

class Primitivos(Instruccion): #hacemos la herencia

    #constructor
    def __init__(self, fila, columna, tipo, valor):
        
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor

    def interpretar(self, tree, table):
        return self.valor