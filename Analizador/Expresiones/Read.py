from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.tipo import TIPO
from tkinter import simpledialog

class Read(Instruccion):

    def __init__(self, fila, columna):
        
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA


    def interpretar(self, tree, table):
        
        # falta arreglar la parte visual cuando se usa el read
        print(tree.getConsola())
        
        entrada = simpledialog.askstring("Read", "El valor ingresado es string por defecto")
        if entrada == None:
            entrada = 'null'
        return entrada