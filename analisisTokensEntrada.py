from Analizador.ply import lex as lex
import re

reserved = {
    'int' : 'TKN_INT',
    'double' : 'TKN_DOUBLE',
    'boolean' : 'TKN_BOOLEAN',
    'char' : 'TKN_CHAR',
    'string' : 'TKN_STRING',

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

#tokens
tokens = (
        'ID',
        'CADENA',
        'CARACTER',
        'ENTERO',
        'DECIMAL',
        'COMENTARIOUNI',
        'COMENTARIOMULTI',
        'OTRO',
        'ENTER',
) + tuple(reserved.values())

def t_ID(t):

    r'[a-zA-Z][a-zA-Z_0-9]*'
    global ultimo_token
    
    t.type = reserved.get(t.value.lower(),'ID')
    if t.type == 'ID':
        ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'normal')
    else:
        ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'reservada')
    return t

def t_CADENA(t):
    r'(\"([^"\\]|(\\n)|(\\\\)|(\\\")|(\\t)|(\\\'))*\")'
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'cadena')
    return t

def t_CARACTER(t):
    r'(\'([^\'\\]|(\\n)|(\\\\)|(\\\")|(\\t)|(\\\'))\')'
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'cadena')
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'numero')
    return t

def t_ENTERO(t):
    r'\d+'
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'numero')
    return t

def t_COMENTARIOMULTI(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += len(re.findall('\\n',t.value))
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'comentario')
    return t

def t_COMENTARIOUNI(t):
    r'\#.*\n'
    t.lexer.lineno += 1
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'comentario')
    return t

def t_OTRO(t):
    r'.'
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'normal')
    return t

def t_ENTER(t):
    r'\n'
    t.lexer.lineno += 1
    global ultimo_token
    ultimo_token = (t.value,t.lineno,obtener_columna(entrada,t.lexpos),'normal')
    return t

def t_error(t):
    t.lexer.skip(1)

def obtener_columna(texto, tok):
    nueva_linea = texto.rfind('\n', 0, tok) + 1
    return (tok - nueva_linea) + 1

ultimo_token = None

lexer = lex.lex(reflags=re.IGNORECASE)

entrada = ''
