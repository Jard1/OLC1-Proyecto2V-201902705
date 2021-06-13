from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO, OperadorRelacional

class Relacional(Instruccion):
    
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
        if isinstance(izquierda, Excepcion): return izquierda

        derecha = self.ExpresionDer.interpretar(tree, table)
        if isinstance(derecha, Excepcion): return derecha

    #**********************************************************IGUAL IGUAL*************************************************************
        
        if self.operador == OperadorRelacional.IGUALIGUAL:

            #-----------------------------ENTERO == ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO == DECIMAL-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO == CADENA------------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.ENTERO):
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) == str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------DECIMAL == DECIMAL---------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------DECIMAL == CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.DECIMAL):
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) == str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------BOOLEANO == BOOLEANO-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------BOOLEANO == CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.BOOLEANO) :
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) == str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------CHARACTER == CHARACTER-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.CHARACTER and self.ExpresionDer.tipo == TIPO.CHARACTER) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------CADENA == CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.CADENA) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) == self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            return Excepcion("NO se puede hacer la operacion == con esos tipos de datos", "Semantico",  self.fila, self.columna)


        #**********************************************************DIFERENTE*************************************************************
        
        elif self.operador == OperadorRelacional.DIFERENTE:

            #-----------------------------ENTERO =! ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO =! DECIMAL-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO =! CADENA------------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.ENTERO):
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) != str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------DECIMAL =! DECIMAL---------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------DECIMAL != CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.DECIMAL):
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) != str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------BOOLEANO != BOOLEANO-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------BOOLEANO != CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.BOOLEANO) :
                return str(self.ValorReal(self.ExpresionIzq.tipo, izquierda)) != str(self.ValorReal(self.ExpresionDer.tipo, derecha))
            #------------------------------CHARACTER != CHARACTER-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.CHARACTER and self.ExpresionDer.tipo == TIPO.CHARACTER) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            #------------------------------CADENA != CADENA-----------------------
            elif (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.CADENA) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) != self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            return Excepcion("NO se puede hacer la operacion =! con esos tipos de datos", "Semantico",  self.fila, self.columna)

        #**********************************************************Menor Que*************************************************************
        elif self.operador == OperadorRelacional.MENORQUE:
            
            #-----------------------------ENTERO < ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) < self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO < DECIMAL----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) < self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------DECIMAL < DECIMAL----------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) < self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------BOOLEANO < BOOLEANO----------------------
            elif self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) < self.ValorReal(self.ExpresionDer.tipo, derecha)
            return Excepcion("NO se puede hacer la operacion < con esos tipos de datos", "Semantico",  self.fila, self.columna)


        #**********************************************************Mayor Que*************************************************************
        
        elif self.operador == OperadorRelacional.MAYORQUE:

            #-----------------------------ENTERO > ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) > self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO < DECIMAL----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) > self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------DECIMAL < DECIMAL----------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) > self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------BOOLEANO < BOOLEANO----------------------
            elif self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) > self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("NO se puede hacer la operacion > con esos tipos de datos", "Semantico",  self.fila, self.columna)

        #**********************************************************Menor Igual*************************************************************
        
        elif self.operador == OperadorRelacional.MENORIGUAL:

            #-----------------------------ENTERO <= ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) <= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO <= DECIMAL----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) <= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------DECIMAL <= DECIMAL----------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) <= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------BOOLEANO <= BOOLEANO----------------------
            elif self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) <= self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            return Excepcion("NO se puede hacer la operacion <= con esos tipos de datos", "Semantico",  self.fila, self.columna)

        #**********************************************************Mayor Igual*************************************************************
        
        elif self.operador == OperadorRelacional.MAYORIGUAL:
            #-----------------------------ENTERO >= ENTERO----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) >= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------ENTERO >= DECIMAL----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) >= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------DECIMAL >= DECIMAL----------------------
            elif self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) >= self.ValorReal(self.ExpresionDer.tipo, derecha)
            #-----------------------------BOOLEANO >= BOOLEANO----------------------
            elif self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO:
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) >= self.ValorReal(self.ExpresionDer.tipo, derecha)
            return Excepcion("NO se puede hacer la operacion > con esos tipos de datos", "Semantico",  self.fila, self.columna)

    def ValorReal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return self.stringToBool(val)
        return str(val)