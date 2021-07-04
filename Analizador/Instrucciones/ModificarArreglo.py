from re import A
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.simbolo import Simbolo
import copy


class ModificarArreglo(Instruccion):
    
    def __init__(self, fila, columna, identificador, expresionesArreglo, expresion):
        
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.expresionesArreglo = expresionesArreglo
        self.expresion = expresion

    def interpretar(self, tree, table):
        
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Excepcion): 
            return value

        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Excepcion("La Variable " + self.identificador + " no ha sido declarada", "Semantico", self.fila, self.columna)
        
        if simbolo.getArreglo(): 
            
            if simbolo.getTipo() == self.expresion.tipo:
                # BUSQUEDA DEL ARREGLO
                value = self.modificarDimensiones(tree, table, copy.copy(self.expresionesArreglo), simbolo.getValor(), value)     #RETORNA EL VALOR SOLICITADO
                if isinstance(value, Excepcion): 
                    return value
                
                return value
            else:
                return Excepcion("El valor asignado no es compatible con el tipo de dato del arreglo.", "Semantico", self.fila, self.columna)
        
        else: 
            return Excepcion("Variable " + self.identificador + " no es un arreglo.", "Semantico", self.fila, self.columna)


    #def getNodo(self):
     #   nodo = NodoAST("MODIFICACION ARREGLO")
      #  nodo.agregarHijo(str(self.identificador))
       # exp = NodoAST("EXPRESIONES DE LAS DIMENSIONES")
        #for expresion in self.expresiones:
        #    exp.agregarHijoNodo(expresion.getNodo())
        #nodo.agregarHijoNodo(exp)
        #nodo.agregarHijoNodo(self.valor.getNodo())
        #return nodo

    def modificarDimensiones(self, tree, table, expresiones, arreglo, valor):

        if len(expresiones) == 0:
            #para retornar el valor
            if isinstance(arreglo, list):
                return Excepcion("Hubo un error al retornar el arreglo, faltan datos", "Semantico", self.fila, self.columna)
            return valor

        if not isinstance(arreglo, list):
            return Excepcion("Accesos de más en un Arreglo", "Semantico", self.fila, self.columna)

        dimension = expresiones.pop(0)
        num = dimension.interpretar(tree, table)

        if isinstance(num, Excepcion): return num
        if dimension.tipo != TIPO.ENTERO:
            return Excepcion("Expresion diferente a ENTERO en Arreglo.", "Semantico", self.fila, self.columna)
        
        value = self.modificarDimensiones(tree, table, copy.copy(expresiones), arreglo[num], valor)
        if isinstance(value, Excepcion): return value
        if value != None:
            arreglo[num] = value

        return None
