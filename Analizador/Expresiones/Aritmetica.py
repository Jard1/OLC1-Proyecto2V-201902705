from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.tipo import OperadorAritmetico


class Aritmetica(Instruccion):
    
    def __init__(self, fila, columna, ExpresionIzq, operador, ExpresionDer):

        self.fila = fila
        self.columna = columna
        self.ExpresionIzq = ExpresionIzq
        self.operador = operador
        self.ExpresionDer = ExpresionDer
        self.tipo = None

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

        #**********************************************************SUMA*************************************************************

        if self.operador == OperadorAritmetico.MAS: 
            #----------------------ENTERO + ENTERO-----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO #Va retornar un entero
                #hacemos la suma
                
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)

            #----------------------- ENTERO + DECIMAL ----------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.DECIMAL #retorna un decimal
                #hacemos la suma
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)

            #------------------------ ENTERO + BOOLEAN ---------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.BOOLEANO) or (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.ENTERO #retorna una cadena 
                #hacemos la concatenacion
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)
            
            #------------------------ ENTERO + CADENA ---------------------
            elif (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.CADENA #retorna una cadena 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #------------------------ DECIMAL + DECIMAL ---------------------
            elif (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL #retorna un decimal 
                #hacemos la concatenacion
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)

            #------------------------ DECIMAL + BOOLEAN ---------------------
            elif (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.BOOLEANO) or (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL #retorna un decimal 
                #hacemos la concatenacion
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)
            
            #------------------------ DECIMAL + CADENA ---------------------
            elif (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.CADENA) or (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.CADENA #retorna una cadena 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #-----------------------------BOLEAN + BOOLEAN------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.BOOLEANO):
                self.tipo = TIPO.BOOLEANO #retorna una BOOLEANO 
                #hacemos la concatenacion
                return  self.ValorReal(self.ExpresionIzq.tipo,izquierda) + self.ValorReal(self.ExpresionDer.tipo,derecha)

            #-----------------------------BOLEAN + CADENA------------------
            elif (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.CADENA or self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.BOOLEANO):
                self.tipo = TIPO.CADENA #retorna una BOOLEANO 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #-----------------------------CHARACTER + CHARACTER------------------
            elif (self.ExpresionIzq.tipo == TIPO.CHARACTER and self.ExpresionDer.tipo == TIPO.CHARACTER):
                self.tipo = TIPO.CADENA #retorna una BOOLEANO 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #-----------------------------CHARACTER + CADENA------------------
            elif (self.ExpresionIzq.tipo == TIPO.CHARACTER and self.ExpresionDer.tipo == TIPO.CADENA or self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.CHARACTER):
                self.tipo = TIPO.CADENA #retorna una BOOLEANO 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #-----------------------------CADENA + CADENA------------------
            elif (self.ExpresionIzq.tipo == TIPO.CADENA and self.ExpresionDer.tipo == TIPO.CADENA):
                self.tipo = TIPO.CADENA #retorna una BOOLEANO 
                #hacemos la concatenacion
                return  str(self.ValorReal(self.ExpresionIzq.tipo,izquierda)) + str(self.ValorReal(self.ExpresionDer.tipo,derecha))

            #Si es una operacion no definida, es un error semantico
            return Excepcion("No se puede hacer una suma con esos tipos de datos", "Semantico", self.fila, self.columna)


        #************************************************************RESTA*************************************************************
        elif self.operador == OperadorAritmetico.MENOS:

            #-------------------------ENTERO - ENTERO-----------------------
            if self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) - self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO - DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) - self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO - BOOLEAN------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.BOOLEANO) or (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.ENTERO
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) - self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------DECIMAL - DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) - self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------DECIMAL - BOOLEAN------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.BOOLEANO) or (self.ExpresionIzq.tipo == TIPO.BOOLEANO and self.ExpresionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) - self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("No se puede hacer una resta con esos tipos de datos", "Semantico" , self.fila, self.columna)

        #************************************************************MULTIPLIACION*************************************************************
        elif self.operador == OperadorAritmetico.POR:
            #-----------------------------ENTERO * ENTERO------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.ENTERO
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) * self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO * DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) * self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            #-----------------------------DECIMAL * DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) * self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("No se puede hacer una multiplicacion con esos tipos de datos", "Semantico" , self.fila, self.columna)

        #************************************************************DIVISION*************************************************************
        
        elif self.operador == OperadorAritmetico.DIV:

            if self.ValorReal(self.ExpresionDer.tipo, derecha) == 0:
                return Excepcion("No se puede dividir entre cero", "Semantico" , self.fila, self.columna)
            #-----------------------------ENTERO / ENTERO------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) / self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO / DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) / self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            #-----------------------------DECIMAL / DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) / self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("No se puede hacer una division con esos tipos de datos", "Semantico" , self.fila, self.columna)

        #************************************************************POTENCIA*************************************************************
        
        elif self.operador == OperadorAritmetico.POTENCIA:
            
            #-----------------------------ENTERO ** ENTERO------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.ENTERO
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) ** self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO ** DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) ** self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            #-----------------------------DECIMAL ** DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) ** self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("No se puede hacer una potencia con esos tipos de datos", "Semantico" , self.fila, self.columna)


        #************************************************************MODULO*************************************************************
        
        elif self.operador == OperadorAritmetico.MOD:
            
            #-----------------------------ENTERO % ENTERO------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) % self.ValorReal(self.ExpresionDer.tipo, derecha)

            #-----------------------------ENTERO % DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO and self.ExpresionDer.tipo == TIPO.DECIMAL) or (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) % self.ValorReal(self.ExpresionDer.tipo, derecha)
            
            #-----------------------------DECIMAL % DECIMAL------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL and self.ExpresionDer.tipo == TIPO.DECIMAL) :
                self.tipo = TIPO.DECIMAL
                return self.ValorReal(self.ExpresionIzq.tipo, izquierda) % self.ValorReal(self.ExpresionDer.tipo, derecha)

            return Excepcion("No se puede hacer modulo con esos tipos de datos", "Semantico" , self.fila, self.columna)

        #************************************************************UMENOS*************************************************************
        
        elif self.operador == OperadorAritmetico.UMENOS:
            #------------------------ENTERO----------------------
            if (self.ExpresionIzq.tipo == TIPO.ENTERO) :
                self.tipo = TIPO.ENTERO
                return - self.ValorReal(self.ExpresionIzq.tipo, izquierda) 
            #------------------------DECIMAL----------------------
            if (self.ExpresionIzq.tipo == TIPO.DECIMAL) :
                self.tipo = TIPO.DECIMAL
                return - self.ValorReal(self.ExpresionIzq.tipo, izquierda) 
            return Excepcion("No se puede hacer negacion unaria con ese tipo de dato", "Semantico" , self.fila, self.columna)

    def ValorReal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return self.stringToBool(str(val))
        return str(val)

    def stringToBool(self,val):
        #pasa todo a minustulas y luego mira si la palabra es true
        return val.lower() in ("true")