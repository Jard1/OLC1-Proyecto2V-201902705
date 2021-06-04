
##****************************************Parte Lexica*****************************************************

tokens = (
    
    #*******************tipos de datos**********************
    'TKN_INT','TKN_DOUBLE','TKN_BOOLEAN','TKN_CHAR','TKN_STRING','TKN_NULL',
    'TKN_NEW',

    #*****************operadores aritmeticos****************
    'TKN_MAS','TKN_MENOS','TKN_POR','TKN_DIV','TKN_POTENCIA','TKN_MOD','TKN_PUNTO',

    'TKN_PTCOMA','TKN_LLAVEIZQ','TKN_LLAVEDER','TKN_PARIZQ','TKN_PARDER','TKN_CORCHETEIZQ','TKN_CORCHETEDER',
    'TKN_COMA','TKN_INCREMENTO','TKN_DECREMENTO',
    
    #********************Relacionales********************
    'TKN_IGUAL_IGUAL','TKN_DIFERENTE','TKN_MENOR',
    'TKN_MAYOR','TKN_MENORI','TKN_MAYORI','TKN_DOSPUNTOS','TKN_IGUAL',
    
    #**********************Logicos***********************
    'TKN_OR','TKN_AND','TKN_NOT','TKN_TRUE','TKN_FALSE',

    #********************Palabras Reservadas*************   
    'TKN_SWITCH','TKN_CASE','TKN_BREAK',

    'TKN_IF','TKN_ELSE','TKN_DEFAULT',

    'TKN_WHILE','TKN_FOR','TKN_CONTINUE','TKN_VOID','TKN_RETURN',

    'TKN_READ','TKN_TOLOWER','TKN_PRINT','TKN_TO_UPPER','TKN_LENGTH','TKN_TRUNCATE',
    'TKN_ROUND','TKN_TYPE_OF','TKN_MAIN',

    'ENTERO', 'DECIMAL'

)

#tipos de datos
t_TKN_INT       = r'int'
t_TKN_DOUBLE    = r'double'
t_TKN_BOOLEAN   = r'boolean'
t_TKN_CHAR      = r'char'
t_TKN_STRING    = r'string'
t_TKN_NULL      = r'null'
t_TKN_NEW       = r'new'

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

t_TKN_TRUE      = r'true'
t_TKN_FALSE     = r'false'

#palabras reservadas
t_TKN_SWITCH    = r'switch'
t_TKN_CASE      = r'case'
t_TKN_BREAK     = r'break'

t_TKN_IF        = r'if'
t_TKN_ELSE      = r'else'
t_TKN_DEFAULT   = r'default'

t_TKN_WHILE     = r'while'
t_TKN_FOR       = r'for'
t_TKN_CONTINUE  = r'continue'

t_TKN_VOID      = r'void'
t_TKN_RETURN    = r'return'

t_TKN_READ      = r'read'
t_TKN_TOLOWER   = r'tolower'
t_TKN_PRINT     = r'print'
t_TKN_TO_UPPER  = r'toupper'
t_TKN_LENGTH    = r'length'
t_TKN_TRUNCATE  = r'truncate'

t_TKN_ROUND     = r'round'
t_TKN_TYPE_OF   = r'typeof'
t_TKN_MAIN      = r'main'

# Caracteres ignorados
t_ignore = " \t"

# Comentario de una línea
def t_ComentarioSimple(t):
    r'\#.*\n'
    t.lexer.lineno += 1    
# Comentario de múltiples líneas
def t_ComentarioMulti(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno = t.value.count("\n")
    
def t_error(t): #LEXICOS
    print('caracter no reconocido: ' + str(t.value[0]))
    # almacenamiento de errores lexicos
    t.lexer.skip(1)

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

# Construyendo el analizador lexico
import ply.lex as lex
lexer = lex.lex()




# Presedencia
precedence = (
    ('left', 'TKN_MAS', 'TKN_MENOS'),
    ('left', 'TKN_POR', 'TKN_DIV', 'TKN_MOD'),
    ('left', 'TKN_POTENCIA'),
    ('right', 'UMENOS'),
    ('left','TKN_IGUAL_IGUAL','TKN_DIFERENTE','TKN_MENOR', 'TKN_MENORI', 'TKN_MAYOR', 'TKN_MAYORI'),
    ('right', 'TKN_NOT'),
    ('left', 'TKN_AND'),
    ('left', 'TKN_OR')
)

#********************************************Parte sintactica********************************************

def p_instrucciones(t):
    '''
    instrucciones : instruccion instrucciones
                    | instruccion
    '''

def p_instruccion(t):
    '''
    instruccion : TKN_CASE TKN_LLAVEIZQ expresion TKN_LLAVEDER TKN_PTCOMA 
    '''
    print('El resultado es: ' + str(t[3]))

def p_expresion_binaria(t):
    '''
    expresion : expresion TKN_MAS expresion
            | expresion TKN_MENOS expresion
            | expresion TKN_POR expresion
            | expresion TKN_DIV expresion
    '''
    if    t[2] == '+': t[0] = t[1] + t[3]
    elif  t[2] == '-': t[0] = t[1] - t[3]
    elif  t[2] == '*': t[0] = t[1] * t[3]
    elif  t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    '''
    expresion : TKN_MENOS expresion %prec UMENOS
    '''
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    '''
    expresion : TKN_PARIZQ expresion TKN_PARDER
    '''
    t[0] = t[2]

def p_expresion_primitivo(t):
    '''
    expresion : ENTERO
            | DECIMAL
    '''
    t[0] = t[1]

def p_error(t):
    print('Error sintactico en: ' + str(t.value))
    # almacenamiento de errores sintacticos

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
print("Archivo ejecutado correctamente :D")