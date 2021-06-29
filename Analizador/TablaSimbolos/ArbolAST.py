class Arbol:

    #constructor
    def __init__(self, instrucciones ):
        
        self.TSglobal = None #tabla de simbolos
        self.excepciones = []
        self.funciones = []
        self.consola = ""

        self.instrucciones = instrucciones

    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def updateConsole(self,cadena):
        self.consola += '> '+ str(cadena) + '\n' #agregamos una nueva linea a la consola

    def getTSGlobal(self):
        return self.TSglobal

    def getInstrucciones(self):
        return self.instrucciones 

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal
        
    def getListaFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    def pushFuncion(self, funcion):
        self.funciones.append(funcion)