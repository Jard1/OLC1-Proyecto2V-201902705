from Analizador.TablaSimbolos.instruccionAbstract import Instruccion
from Analizador.TablaSimbolos.Excepcion import Excepcion
from Analizador.TablaSimbolos.tipo import TIPO
from Analizador.TablaSimbolos.simbolo import Simbolo
from Analizador.TablaSimbolos.tipo import OperadorAritmetico
from Analizador.TablaSimbolos.nodoASTabstract import NodoASTabstract


class incrementoDecremento(Instruccion):

    def __init__(self, fila, columna , identificador, tipoOperacion ):
        
        self.fila = fila
        self.columna = columna

        self.identificador = identificador
        self.tipoOperacion = tipoOperacion

    def interpretar(self, tree, table):
        
        simbolo = table.getTabla(self.identificador.lower()) #Buscamos la variable
        
        if isinstance(simbolo, Excepcion): 
            return simbolo

        value = simbolo.getValor()
        if isinstance(value, Excepcion): 
            return value

        if simbolo.getTipo() == TIPO.ENTERO or simbolo.getTipo() == TIPO.DECIMAL:

            if self.tipoOperacion == OperadorAritmetico.INCREMENTO:
                value = value + 1
            elif self.tipoOperacion == OperadorAritmetico.DECREMENTO:
                value = value - 1

            simbolo.setValor(value)
            result = table.actualizarTabla(simbolo)

        else:
            return Excepcion("La operacion incremento o decremento solo se puede realizar en enteros o decimales","Semantico" , self.fila, self.columna)
        
        self.tipo = simbolo.getTipo()
        return value


    def getNodo(self):
        nodo = NodoASTabstract("Incremento/Decremento")
        nodo.agregarHijo(str(self.identificador))
        return nodo