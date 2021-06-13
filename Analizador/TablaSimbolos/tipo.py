from enum import Enum

class TIPO(Enum):
    ENTERO      = 0
    DECIMAL     = 1
    BOOLEANO    = 2
    CHARACTER   = 3
    CADENA      = 4
    NULO        = 5
    ARREGLO     = 6

class OperadorAritmetico(Enum):
    MAS         = 0
    MENOS       = 1
    POR         = 2
    DIV         = 3
    POTENCIA    = 4
    MOD         = 5
    UMENOS      = 7

class OperadorRelacional(Enum):
    MENORIGUAL      = 0
    MAYORIGUAL      = 1
    MENORQUE        = 2
    MAYORQUE        = 3
    IGUALIGUAL      = 4
    DIFERENTE       = 5

class OperadorLogico(Enum):
    NOT     = 1
    AND     = 2
    OR      = 3