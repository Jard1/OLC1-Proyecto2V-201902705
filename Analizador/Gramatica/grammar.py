def p_instrucciones(t):
    '''
    instrucciones : instrucciones instruccion
                    | instruccion
    '''

def p_instruccion(t):
    '''
    instruccion : expresion TKN_PTCOMA
                | expresion
                | declararVar TKN_PTCOMA --
                | declararVar --
                | asignacion -- 
                | instIF  --
                | instSwitch  --
                | instBreak  --
                | instWhile  --
                | instFor  -- 
                | instMain  --
                | instPrint  --
    '''
    print('El resultado es: ' + str(t[3]))

def p_expresion(t):
    '''
    expresion   : expresion TKN_MAS expresion
                | expresion TKN_MENOS expresion
                | expresion TKN_POR expresion
                | expresion TKN_DIV expresion
                | expresion TKN_POTENCIA expresion
                | expresion TKN_MOD expresion

                | expresion TKN_IGUAL_IGUAL expresion
                | expresion TKN_DIFERENTE expresion
                | expresion TKN_AND expresion
                | expresion TKN_OR expresion
                | expresion TKN_MAYORI expresion
                | expresion TKN_MENORI expresion
                | expresion TKN_MAYOR expresion
                | expresion TKN_MENOR expresion
                | TKN_NOT expresion
                | TKN_PARIZQ tipoDato TKN_PARDER expresion %prec cast --
                | ENTERO
                | ID --
                | DECIMAL
                | TKN_TRUE
                | TKN_FALSE
    '''
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






def p_declararVar(t):
    '''
    declararVar :
    '''

def p_asignacion(t):
    '''
    asignacion :
    '''

def p_instIF(t):
    '''
    instIF :
    '''
def p_instSwitch(t):
    '''
    instSwitch :
    '''

def p_instBreak(t):
    '''
    instBreak :
    '''

def p_instWhile(t):
    '''
    instWhile :
    '''

def p_instFor(t):
    '''
    instFor :
    '''

def p_instMain(t):
    '''
    instMain :
    '''

def p_instPrint(t):
    '''
    instPrint :
    '''

def p_declararVar(t):
    '''
    declararVar : tipoDato ID TKN_IGUAL expresion
                | tipoDato ID
    '''
