from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.tipo import TIPO

class Read(Instruccion):

    def __init__(self, fila, columna):
        
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA


    def interpretar(self, tree, table):
        
        print(tree.getConsola()) #IMPRIME LA CONSOLA
        print("Ingreso a un READ. Ingrese el valor")
        tree.setConsola("")     #RESETEA LA CONSOLA
        
        # ESTO SOLO ES DE EJEMPLO realmente tiene que estar en un messaguebox
        
        lectura = input() # OBTENERME EL VALOR INGRESADO
        return lectura