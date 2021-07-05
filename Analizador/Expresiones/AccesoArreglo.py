  
from re import A
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.simbolo import Simbolo
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract
import copy


class AccesoArreglo(Instruccion):
    def __init__(self, fila, columna, identificador, expresiones):
        self.identificador = identificador
        self.expresiones = expresiones
        self.fila = fila
        self.columna = columna


    def interpretar(self, tree, table):

        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Excepcion("La variable " + self.identificador + " no ha sido declarada", "Semantico", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        
        if simbolo.getArreglo():

            value = self.buscarDimensiones(tree, table, copy.copy(self.expresiones), simbolo.getValor())     #RETORNA EL VALOR SOLICITADO
            
            if isinstance(value, Excepcion): 
                return value
            if isinstance(value, list):
                return Excepcion("Hubo un error al retornar el arreglo, faltan datos", "Semantico", self.fila, self.columna)

            return value

        else: 
            return Excepcion("La variable " + self.identificador + " no es un Arreglo.", "Semantico",self.fila, self.columna)

    def buscarDimensiones(self, tree, table, expresiones, arreglo):
        
        valor = None

        if len(expresiones) == 0:
            #para retornar el valor
            return arreglo
        if not isinstance(arreglo, list):
            return Excepcion("Accesos de más en un Arreglo", "Semantico", self.fila, self.columna)
        
        dimension = expresiones.pop(0)
        
        num = dimension.interpretar(tree, table)

        if isinstance(num, Excepcion): 
            return num
        if dimension.tipo != TIPO.ENTERO:
            return Excepcion("La dimension del arreglo tiene que ser un ENTERO", "Semantico", self.fila, self.columna)
        
        valor = self.buscarDimensiones(tree, table, copy.copy(expresiones), arreglo[num])
            
        return valor

    
    def getNodo(self):
        nodo = NodoASTabstract("Acceso Arreglo")
        nodo.agregarHijo(str(self.identificador))
        exp = NodoASTabstract("Dimensiones")
        for expresion in self.expresiones:
            exp.agregarHijoNodo(expresion.getNodo())
            nodo.agregarHijoNodo(exp)
        return nodo
