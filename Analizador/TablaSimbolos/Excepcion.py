class Excepcion:
    
    def __init__(self, descripcion, tipo, fila, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def toString(self):
        return "Error "+self.tipo + ": " + self.descripcion + " en (Linea: " + str(self.fila) + ", Col: " + str(self.columna) + ")"

    def getDescripcion(self):
        return self.descripcion

    def getTipo(self):
        return self.tipo

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna