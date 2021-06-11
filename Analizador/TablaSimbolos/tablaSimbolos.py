from TablaSimbolos.Excepcion import Excepcion

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
            if id in self.tabla :
                #si esta en la tabla, lo retorna
                return self.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None

    #---------------------------------------------Agregar una variable
    def setTabla(self, simbolo):      
       
        if simbolo.id in self.tabla : 
            #si el id del simbolo que buscamos, esta en la tabla
            return Excepcion("La variable " + simbolo.id + " ya fue declarada", "Semantico", simbolo.fila, simbolo.columna)
        else:
            #si no lo encuentra, lo agregamos a la tabla
            self.tabla[simbolo.id] = simbolo
            return None

    #---------------------------------------------Actualizar tabla
    def actualizarTabla(self, simbolo):

        tablaActual = self

        while tablaActual != None:
            
            if simbolo.id in self.tabla :
                #cambiamos por el nuevo valor
                self.tabla[simbolo.id].setTipo(simbolo.getTipo())
                self.tabla[simbolo.id].setValor(simbolo.getValor())
                return "Valor Actualizado"
            else:
                tablaActual = tablaActual.anterior
        return None
        