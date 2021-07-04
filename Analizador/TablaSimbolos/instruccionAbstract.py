from abc import ABC, abstractmethod #para saber cuando usa una clase abstracta o no

class Instruccion(ABC):

    #constructor
    def __init__(self, fila, columna):
        
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        super().__init__()  #llamamos al constructor padre

    @abstractmethod
    def interpretar(self, tree, table): #arbol ast, tabla de simbolos
        pass