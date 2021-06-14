from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.tipo import TIPO
from TablaSimbolos.tablaSimbolos import TablaSimbolos

class If(Instruccion):

    def __init__(self, fila, columna, expCondicion, instruccionesIf, instruccionesElse, ElseIf):
        self.fila = fila
        self.columna = columna
        self.condicion = expCondicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOLEANO:
            if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                    if isinstance(result, Excepcion) :
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
            else:               #ELSE
                if self.instruccionesElse != None:
                    nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instruccionesElse:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString()) 
                elif self.elseIf != None:
                    result = self.elseIf.interpretar(tree, table)
                    if isinstance(result, Excepcion): return result

        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
    