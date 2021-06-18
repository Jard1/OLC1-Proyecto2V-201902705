from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO

class TablaSimbolos:
    
    #contructor
    def __init__(self, tablaAnterior = None):
        
        self.tabla = {}
        self.tablaAnterior = tablaAnterior #la tabla de simbolos anterior (para ver lo de los ambitos)
        #self.funciones = []

    #------------------------------------------Obtener variable

    def getTabla(self, id):
        
        tablaActual = self      

        #buscamos en todas las tablas enlazadas a la variable
        while tablaActual != None:
            if id in tablaActual.tabla :
                #si esta en la tabla, lo retorna
                return tablaActual.tabla[id]
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
            
            if simbolo.id.lower() in tablaActual.tabla :
                
                #si es del mismo tipo, o no tiene un tipo definido , o le asignan el valor de null
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id.lower()].getTipo() == TIPO.NULO or simbolo.getTipo() == TIPO.NULO :

                    #cambiamos por el nuevo valor
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    return None
                return Excepcion ("El valor asignado no es compatible con el tipo de dato de la variable", "Semantico" ,simbolo.getFila(), simbolo.getColumna())
            else:

                tablaActual = tablaActual.tablaAnterior
        
        return Excepcion ("No se ha declarado la variable que esta asignando","Semantico" ,simbolo.getFila(), simbolo.getColumna())
        