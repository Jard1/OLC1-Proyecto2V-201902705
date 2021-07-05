from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO, OperadorLogico
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract

class Casteos(Instruccion):
    
    def __init__(self, fila, columna, tipo, expresion):

        self.fila = fila
        self.columna = columna

        self.expresion = expresion
        self.tipo = tipo

    
    def interpretar(self, tree, table):

        valor = self.expresion.interpretar(tree, table)
        
        #-------------------------------------------TIPO DESEADO ENTERO---------------------------------------------

        if self.tipo == TIPO.ENTERO:
            #---------------------ENTRADA DECIMAL-------------------
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    #hacemos el casteo dependiendo del tipo de dato y del valor
                    return int(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a INT", "Semantico", self.fila, self.columna)

            #-----------------------ENTRADA CHAR--------------------
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return ord(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a INT", "Semantico", self.fila, self.columna)

            #-----------------------ENTRADA STRING--------------------
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a INT", "Semantico", self.fila, self.columna)

            return Excepcion("NO se puede castear a INT con ese tipo de dato", "Semantico", self.fila, self.columna)
        
        #-------------------------------------------TIPO DESEADO DECIMAL-----------------------------------------------

        if self.tipo == TIPO.DECIMAL:
            #---------------------------ENTRADA ENTERO-------------------------
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return float(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a DOUBLE", "Semantico", self.fila, self.columna)
            
            #-------------------------ENTRADA CHAR-----------------------------
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return float(ord(self.ValorReal(self.expresion.tipo, valor)))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a DOUBLE", "Semantico", self.fila, self.columna)
            
            #-------------------------ENTRADA CADENA-----------------------------
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, valor))
                except:
                   return Excepcion("El valor ingresado NO se pudo castear a DOUBLE", "Semantico", self.fila, self.columna) 

            return Excepcion("NO se puede castear a DOUBLE con ese tipo de dato", "Semantico", self.fila, self.columna)

        #-------------------------------------------TIPO DESEADO CADENA-----------------------------------------------

        if self.tipo == TIPO.CADENA:
            #---------------------------ENTRADA ENTERO-------------------------
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a STRING", "Semantico", self.fila, self.columna)

            #-----------------------ENTRADA DECIMAL--------------------
            elif self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return str(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a INT", "Semantico", self.fila, self.columna)

            return Excepcion("NO se puede castear a STRING con ese tipo de dato", "Semantico", self.fila, self.columna)

        #-------------------------------------------TIPO DESEADO CHAR-----------------------------------------------

        if self.tipo == TIPO.CHARACTER:
            #---------------------------ENTRADA ENTERO-------------------------
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return chr(self.ValorReal(self.expresion.tipo, valor))
                except:
                    return Excepcion("El valor ingresado NO se pudo castear a CHAR", "Semantico", self.fila, self.columna)

            return Excepcion("NO se puede castear a CHAR con ese tipo de dato", "Semantico", self.fila, self.columna)

        #-------------------------------------------TIPO DESEADO boolean-----------------------------------------------

        if self.tipo == TIPO.BOOLEANO:
            #---------------------------ENTRADA CADENA-------------------------
            if self.expresion.tipo == TIPO.CADENA:
                try:
                    valorRealString = self.ValorReal(self.expresion.tipo, valor)

                    if valorRealString.lower() == 'true' or  valorRealString.lower() == 'false':
                        return self.stringToBool(self.ValorReal(self.expresion.tipo, valor))

                    return Excepcion("NO se puede castear a BOOLEAN con ese valor de string", "Semantico", self.fila, self.columna)

                except:
                    return Excepcion("El valor ingresado NO se pudo castear a booleano", "Semantico", self.fila, self.columna)

            return Excepcion("NO se puede castear a BOOLEAN con ese tipo de dato", "Semantico", self.fila, self.columna)

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

    def getNodo(self):
        nodo = NodoASTabstract("Casteos")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo