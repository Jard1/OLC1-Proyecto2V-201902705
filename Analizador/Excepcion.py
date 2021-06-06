class Excepcion:
    
    def __init__(self, descripcion, tipo, fila, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def toString(self):
        return self.tipo + " ; " + self.descripcion + " (" + str(self.fila) + "," + str(self.columna) + ")"

    