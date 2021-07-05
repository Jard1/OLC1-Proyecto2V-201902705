from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO, OperadorLogico
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Logica(Instruccion):

    def __init__(self, fila, columna, ExpresionIzq, operador, ExpresionDer):

        self.fila = fila
        self.columna = columna
        self.ExpresionIzq = ExpresionIzq
        self.operador = operador
        self.ExpresionDer = ExpresionDer
        self.tipo  = TIPO.BOOLEANO

    def interpretar(self, tree, table):

        #Obtenemos los valores que vienen
        izquierda = self.ExpresionIzq.interpretar(tree, table)
        
        if isinstance(izquierda, Excepcion): 
            return izquierda

        if self.ExpresionDer != None:
            #Es una operacion binara
            derecha = self.ExpresionDer.interpretar(tree, table)
            if isinstance(derecha, Excepcion): 
                return derecha

        #Hacemos la operacion deseada
        #**********************************************************OR*************************************************************
        if self.operador == OperadorLogico.OR: 
            #----------------------BOOL || BOOL-----------------------
            if self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return  self.stringToBool(str(izquierda)) or self.stringToBool(str(derecha))
            return Excepcion("No se puede hacer OR || con ese tipo de dato", "Semantico" , self.fila, self.columna)
        #**********************************************************AND*************************************************************
        elif self.operador == OperadorLogico.AND:
            if self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return  self.stringToBool(str(izquierda)) and self.stringToBool(str(derecha))
            return Excepcion("No se puede hacer AND && con ese tipo de dato", "Semantico" , self.fila, self.columna)
        #**********************************************************NOT*************************************************************
        elif self.operador == OperadorLogico.NOT:
            if self.ExpresionIzq.tipo == TIPO.BOOLEANO:
                return  not self.stringToBool(str(izquierda))
            return Excepcion("No se puede hacer NOT ! con ese tipo de dato", "Semantico" , self.fila, self.columna)


    def stringToBool(self,val):
        #pasa todo a minustulas y luego mira si la palabra es true
        return val.lower() in ("true")


    def getNodo(self):
        nodo = NodoASTabstract("Logica")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.ExpresionIzq.getNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.ExpresionDer.getNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.ExpresionIzq.getNodo())
        
        return nodo