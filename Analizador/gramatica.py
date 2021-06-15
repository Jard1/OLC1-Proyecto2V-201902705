#*****************************************************************************************************************
#                                                       Parte Lexica                                             *
#*****************************************************************************************************************
from TablaSimbolos.Excepcion import Excepcion
errores = []

#tipos de datos
tiposDatos = {
    'int' : 'TKN_INT',
    'double' : 'TKN_DOUBLE',
    'boolean' : 'TKN_BOOLEAN',
    'char' : 'TKN_CHAR',
    'string' : 'TKN_STRING',
}

reservadas = {
    'null' : 'TKN_NULL',
    'new' : 'TKN_NEW',
    'var' : 'TKN_VAR',

    'true' : 'TKN_TRUE',
    'false' : 'TKN_FALSE',

    'switch' : 'TKN_SWITCH',
    'case' : 'TKN_CASE',
    'break' : 'TKN_BREAK',

    'if' : 'TKN_IF',
    'else' : 'TKN_ELSE',
    'default' : 'TKN_DEFAULT',

    'while' : 'TKN_WHILE',
    'for' : 'TKN_FOR',
    'continue' : 'TKN_CONTINUE',

    'void' : 'TKN_VOID',
    'return' : 'TKN_RETURN',

    'read' : 'TKN_READ',
    'tolower' : 'TKN_TOLOWER',
    'print' : 'TKN_PRINT',
    'toupper' : 'TKN_TO_UPPER',
    'length' : 'TKN_LENGTH',
    'truncate' :'TKN_TRUNCATE',

    'round' : 'TKN_ROUND',
    'typeof' : 'TKN_TYPE_OF',
    'main' : 'TKN_MAIN'
}

tokens = [
    #*****************operadores aritmeticos****************
    'TKN_MAS','TKN_MENOS','TKN_POR','TKN_DIV','TKN_POTENCIA','TKN_MOD','TKN_PUNTO',

    'TKN_PTCOMA','TKN_LLAVEIZQ','TKN_LLAVEDER','TKN_PARIZQ','TKN_PARDER','TKN_CORCHETEIZQ','TKN_CORCHETEDER',
    'TKN_COMA','TKN_INCREMENTO','TKN_DECREMENTO',
    
    #********************Relacionales********************
    'TKN_IGUAL_IGUAL','TKN_DIFERENTE','TKN_MENOR',
    'TKN_MAYOR','TKN_MENORI','TKN_MAYORI','TKN_DOSPUNTOS','TKN_IGUAL',
    
    #**********************Logicos***********************
    'TKN_OR','TKN_AND','TKN_NOT',

    'ENTERO', 'DECIMAL', 'ID', 'CADENA', 'CHARACTER'

] + list(tiposDatos.values()) + list(reservadas.values())

#operadores aritmeticos
t_TKN_MAS       = r'\+'
t_TKN_MENOS     = r'-'
t_TKN_POR       = r'\*'
t_TKN_DIV       = r'/'
t_TKN_POTENCIA  = r'\*\*'
t_TKN_MOD       = r'%'
t_TKN_PUNTO     = r'\.'

t_TKN_PTCOMA        = r';'
t_TKN_LLAVEIZQ      = r'\{'
t_TKN_LLAVEDER      = r'\}'
t_TKN_PARIZQ        = r'\('
t_TKN_PARDER        = r'\)'
t_TKN_CORCHETEIZQ   = r'\['
t_TKN_CORCHETEDER   = r'\]'
t_TKN_COMA          = r'\,'
t_TKN_INCREMENTO    = r'\+\+'
t_TKN_DECREMENTO    = r'--'

#relacionales
t_TKN_DIFERENTE     = r'=!'
t_TKN_IGUAL_IGUAL   = r'=='
t_TKN_MENOR         = r'<'
t_TKN_MAYOR         = r'>'
t_TKN_MENORI        = r'<='
t_TKN_MAYORI        = r'>='

t_TKN_DOSPUNTOS     = r':'
t_TKN_IGUAL         = r'='

#logicos
t_TKN_OR        = r'\|\|'
t_TKN_AND       = r'&&'
t_TKN_NOT       = r'!'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es demasiado grande '%d'" % t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large '%d'" % t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    #r'(\".*?\")'
    r'(\".*(\\\")*?\")'
    t.value = t.value[1:-1] # para quitar las comillas dobles
    #caracteres especiales
    t.value = str(t.value).replace('\\n', '\n').replace('\\\"', '\"').replace('\\t', '\t').replace('\\\'', '\'').replace('\\\\', '\\')
    return t

def t_CHARACTER(t):
    #r'(\".*?\")'
    r'(\'.\')|(\'\\n\')|(\'\\r\')|(\'\\t\')|(\'\\\"\')|(\'\\\'\')|(\'\\\\\')'
    t.value = t.value[1:-1] # para quitar las comillas dobles
    #caracteres especiales
    return t

# Comentario de múltiples líneas
def t_ComentarioMulti(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario de una línea
def t_ComentarioSimple(t):
    r'\#.*\n'
    t.lexer.lineno += 1    

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t): #LEXICOS
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, get_column(input, t)))
    print('caracter no reconocido: ' + str(t.value[0]))
    # almacenamiento de errores lexicos
    t.lexer.skip(1)

# Compute column.
# input is the input text string
# token is a token instance
def get_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador lexico
import re
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)




# Presedencia
precedence = (
    ('left', 'TKN_MAS', 'TKN_MENOS'),
    ('left', 'TKN_POR', 'TKN_DIV', 'TKN_MOD'),
    ('left', 'TKN_POTENCIA'),
    ('right', 'UMENOS'),
    ('left', 'TKN_OR'),
    ('left', 'TKN_AND'),
    ('right', 'UNOT'),   
    ('left','TKN_IGUAL_IGUAL','TKN_DIFERENTE','TKN_MENOR', 'TKN_MENORI', 'TKN_MAYOR', 'TKN_MAYORI'),
)

#*****************************************************************************************************************************
#                                                         Parte sintactica                                                   *
#*****************************************************************************************************************************

from Instrucciones.Declaracion import Declaracion
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.imprimir import Imprimir

from Expresiones.Primitivos import Primitivos
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Expresiones.Identificador import Identificador

from TablaSimbolos.tipo import TIPO
from TablaSimbolos.instruccionAbstract import Instruccion
from TablaSimbolos.tipo import OperadorAritmetico, OperadorRelacional, OperadorLogico

#------------------------------------------Inicio gramatica-----------------------------------------
def p_s(t):
    's  :   instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t):
    'instrucciones : instrucciones instruccion'

    if t[2] != "":
        t[1].append(t[2]) #se agrega la lista de instrucciones
    t[0] = t[1] #se sube a la produccion s

def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = [] #si no hay ninguna instruccion
    else:    
        t[0] = [t[1]]

def p_finalizacion(t): #esto es porque el punto y coma es opcional
    '''
    finalizacion : TKN_PTCOMA
                 | 
    '''
    t[0]=None
#--------------------------------------------Instruccion----------------------------------------------

def p_instruccion(t):
    '''
    instruccion : instPrint finalizacion
                | expresion finalizacion 
                | declararVar finalizacion
                | asignacion finalizacion
                | instIF
                | 
    '''
    t[0] = t[1]

#--------------------------------------------Print------------------------------------------------------    
def p_instPrint(t):
    'instPrint : TKN_PRINT TKN_PARIZQ expresion TKN_PARDER'
    t[0] = Imprimir(t.lineno(1), get_column(input, t.slice[1]),t[3])   

#--------------------------------------------Expresion---------------------------------------------------
def p_expresion_binaria(t):
    '''
    expresion : expresion TKN_MAS expresion
            | expresion TKN_MENOS expresion
            | expresion TKN_POR expresion
            | expresion TKN_DIV expresion
            | expresion TKN_POTENCIA expresion
            | expresion TKN_MOD expresion
            | expresion TKN_IGUAL_IGUAL expresion
            | expresion TKN_DIFERENTE expresion
            | expresion TKN_MENOR expresion
            | expresion TKN_MAYOR expresion
            | expresion TKN_MENORI expresion
            | expresion TKN_MAYORI expresion
            | expresion TKN_OR expresion
            | expresion TKN_AND expresion
    '''
    if  t[2] == '+': 
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.MAS, t[3])
    elif  t[2] == '-': 
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.MENOS, t[3])
    elif  t[2] == '*':
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.POR, t[3])
    elif  t[2] == '/': 
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.DIV, t[3])
    elif  t[2] == '**': 
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.POTENCIA, t[3])
    elif  t[2] == '%': 
        t[0] = Aritmetica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorAritmetico.MOD, t[3])


    elif  t[2] == '==': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.IGUALIGUAL, t[3])
    elif  t[2] == '=!': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.DIFERENTE, t[3])
    elif  t[2] == '<': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.MENORQUE, t[3])
    elif  t[2] == '>': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.MAYORQUE, t[3])
    elif  t[2] == '<=': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.MENORIGUAL, t[3])
    elif  t[2] == '>=': 
        t[0] = Relacional(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorRelacional.MAYORIGUAL, t[3])
    
    
    elif  t[2] == '||':
        t[0] = Logica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorLogico.OR, t[3])
    elif  t[2] == '&&':
        t[0] = Logica(t.lineno(2), get_column(input, t.slice[2]), t[1], OperadorLogico.AND, t[3])

def p_expresion_not(t):
    '''
    expresion : TKN_NOT expresion %prec UNOT
    '''
    t[0] = Logica(t.lineno(1), get_column(input, t.slice[1]), t[2], OperadorLogico.NOT, None)
    
def p_expresion_unaria(t):
    '''
    expresion : TKN_MENOS expresion %prec UMENOS
    '''
    #t[0] = -t[2]
    t[0] = Aritmetica(t.lineno(1), get_column(input, t.slice[1]), t[2], OperadorAritmetico.UMENOS, None)

def p_expresion_agrupacion(t):
    '''
    expresion : TKN_PARIZQ expresion TKN_PARDER
    '''
    t[0] = t[2]

#-----------------PRIMITIVOS-------------------
def p_expresion_ID(t):
    '''expresion : ID'''
    t[0] = Identificador(t.lineno(1), get_column(input, t.slice[1]), t[1])

def p_expresion_ENTERO(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.ENTERO, t[1])

def p_expresion_DECIMAL(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.DECIMAL, t[1])

def p_expresion_CADENA(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.CADENA, t[1])

def p_expresion_CHARACTER(t):
    '''expresion : CHARACTER'''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.CHARACTER, t[1])

def p_expresion_boolean(t):
    '''expresion : TKN_FALSE
                 | TKN_TRUE
    '''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.BOOLEANO , t[1])

def p_expresion_null(t):
    '''expresion : TKN_NULL'''
    t[0] = Primitivos(t.lineno(1), get_column(input, t.slice[1]), TIPO.NULO , t[1])
#------------------------------------------Manejo de errores-------------------------------------------
def p_instruccion_error(t):
    'instruccion        : error TKN_PTCOMA'
    errores.append(Excepcion("Error con el caracter " + str(t[1].value) , "Sintáctico" , t.lineno(1), get_column(input, t.slice[1])))
    t[0] = ""

#-----------------------------------------------declararVar----------------------------------------------

def p_declararVar(t):
    'declararVar : TKN_VAR ID'
    t[0] = Declaracion(t.lineno(1), get_column(input, t.slice[1]),t[2])

def p_declararVarAsignacion(t):
    'declararVar : TKN_VAR ID TKN_IGUAL expresion'
    t[0] = Declaracion(t.lineno(1), get_column(input, t.slice[1]),t[2],t[4])

#------------------------------------------------asignacion------------------------------------------------

def p_asignacion(t):
    'asignacion : ID TKN_IGUAL expresion'
    t[0] = Asignacion(t.lineno(1), get_column(input, t.slice[1]),t[1],t[3])

#-------------------------------------------------instIF----------------------------------------------------

def p_instIF_simple(t):
    'instIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER'
    t[0] = If(t.lineno(1), get_column(input, t.slice[1]),t[3], t[6], None, None)

def p_instIF_else(t):
    'instIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER TKN_ELSE TKN_LLAVEIZQ instrucciones TKN_LLAVEDER'
    t[0] = If(t.lineno(1), get_column(input, t.slice[1]),t[3], t[6], t[10], None)

def p_instIF_elseIF(t):
    'instIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER instIF'
    t[0] = If(t.lineno(1), get_column(input, t.slice[1]),t[3], t[6], None, t[8])

import ply.yacc as yacc
parser = yacc.yacc()
input = ''

def getErrores():
    return errores

def parse(inp):
    global errores
    global lexer
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)



f = open("./entrada.txt", "r")
entrada = f.read()

#print(parse(entrada))
#parser.parse(input)
#print("Archivo ejecutado correctamente :D")

from TablaSimbolos.ArbolAST import Arbol
from TablaSimbolos.tablaSimbolos import TablaSimbolos

instrucciones = parse(entrada) #ARBOL AST
ast = Arbol(instrucciones)

TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)

#Para mostrar la lista DE ERRORES LEXICOS Y SINTACTICOS
for error in errores:                   
    ast.getExcepciones().append(error)
    ast.updateConsole(error.toString())

# realizar las instrucciones deseadas, que estan guardadas en el ast
for instruccion in ast.getInstrucciones():
    value = instruccion.interpretar(ast,TSGlobal)
    if isinstance(value, Excepcion) :
        ast.getExcepciones().append(value)
        ast.updateConsole(value.toString())

print(ast.getConsola())