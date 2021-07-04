#from re import A
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.simbolo import Simbolo
import copy


class DeclaracionArrNew(Instruccion):

    def __init__(self,  fila, columna, tipoizq, dimension, identificador, tipoder, expresionesDimension):
        
        self.fila = fila
        self.columna = columna
        
        self.tipoizq = tipoizq
        self.dimension = dimension
        self.identificador = identificador
        self.tipoDer = tipoder
        self.expresionesDimension = expresionesDimension
        self.arreglo = True

    def interpretar(self, tree, table):

        if self.tipoizq == self.tipoDer:

            if self.dimension == len(self.expresionesDimension):

                value = self.crearDimensiones(tree, table,copy.copy(self.expresionesDimension))     #RETORNA EL ARREGLO DE DIMENSIONES
                
                if isinstance(value, Excepcion): 
                    return value
                
                simbolo = Simbolo(self.fila, self.columna, str(self.identificador),value, self.tipoizq, self.arreglo)
                result = table.setTabla(simbolo)
                
                if isinstance(result, Excepcion): 
                    return result
                
                return None

            else:                
                return Excepcion("La dimension de declaracion y asignacion tienen que ser iguales","Semantico", self.fila, self.columna)
        else:
            return Excepcion("El tipo de dato de declaracion y asignacion tienen que ser los mismos","Semantico", self.fila, self.columna)


    def crearDimensiones(self, tree, table, expresiones):
        
        arreglo = []
        #para sacar la recursividad
        if len(expresiones) == 0:
            return 'null' #tipo de dato por defecto

        Valordimension = expresiones.pop(0) #sacamos la primera posicion del arreglo
        
        numero = Valordimension.interpretar(tree, table)
        if isinstance(numero, Excepcion): 
            return numero

        if Valordimension.tipo != TIPO.ENTERO:
            return Excepcion("El tamaño del arreglo tiene que ser un entero", "Semantico", self.fila, self.columna)
        
        cont = 0
        while cont < numero:
            #creamos el arreglo
            arreglo.append(self.crearDimensiones(tree, table, copy.copy(expresiones)))
            cont += 1
        return arreglo