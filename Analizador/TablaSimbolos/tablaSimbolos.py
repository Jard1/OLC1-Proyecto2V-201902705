from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO

class TablaSimbolos:
    
    #contructor
    def __init__(self, tablaAnterior = None):
        
        self.tablaAnterior = tablaAnterior #la tabla de simbolos anterior (para ver lo de los ambitos)
        
        self.tabla = {}
        self.funciones = []

    #------------------------------------------Obtener variable

    def getTabla(self, id):
        
        tablaActual = self      

        #buscamos en todas las tablas enlazadas a la variable
        while tablaActual != None:
            if id.lower() in self.tabla :
                #si esta en la tabla, lo retorna
                return self.tabla[id.lower()]
            else:
                tablaActual = tablaActual.tablaAnterior
        return None

    #---------------------------------------------Agregar una variable
    def setTabla(self, simbolo):      
       
        if simbolo.id.lower() in self.tabla : 
            #si el id del simbolo que buscamos, esta en la tabla
            return Excepcion("La variable " + simbolo.id + " ya fue declarada", "Semantico", simbolo.fila, simbolo.columna)
        else:
            #si no lo encuentra, lo agregamos a la tabla
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    #---------------------------------------------Actualizar tabla
    def actualizarTabla(self, simbolo):

        tablaActual = self

        while tablaActual != None:
            
            if simbolo.id.lower() in self.tabla :
                
                #si es del mismo tipo, o no tiene un tipo definido , o le asignan el valor de null
                if self.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or self.tabla[simbolo.id.lower()].getTipo() == TIPO.NULO or simbolo.getTipo() == TIPO.NULO :

                    #cambiamos por el nuevo valor
                    self.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    self.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    return None
                return Excepcion ("El valor asignado no es compatible con el tipo de dato de la variable", "Semantico" ,simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.tablaAnterior
        return Excepcion ("No se ha declarado la variable que esta asignando","Semantico" ,simbolo.getFila(), simbolo.getColumna())
        