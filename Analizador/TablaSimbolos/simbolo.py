class Simbolo:

    #contructor
    def __init__(self, fila, columna, identificador, valor, tipo ):
        
        self.fila = fila
        self.columna = columna
        self.id = identificador
        self.valor = valor
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getValor(self):
        return self.valor
    def setValor(self, valor):
        self.valor = valor

    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna