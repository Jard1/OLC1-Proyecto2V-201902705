
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTKN_MASTKN_MENOSleftTKN_PORTKN_DIVTKN_MODleftTKN_POTENCIArightUMENOSleftTKN_ORleftTKN_ANDrightUNOTleftTKN_IGUAL_IGUALTKN_DIFERENTETKN_MENORTKN_MENORITKN_MAYORTKN_MAYORICADENA CHARACTER DECIMAL ENTERO ID TKN_AND TKN_BOOLEAN TKN_BREAK TKN_CASE TKN_CHAR TKN_COMA TKN_CONTINUE TKN_CORCHETEDER TKN_CORCHETEIZQ TKN_DECREMENTO TKN_DEFAULT TKN_DIFERENTE TKN_DIV TKN_DOSPUNTOS TKN_DOUBLE TKN_ELSE TKN_FALSE TKN_FOR TKN_IF TKN_IGUAL TKN_IGUAL_IGUAL TKN_INCREMENTO TKN_INT TKN_LENGTH TKN_LLAVEDER TKN_LLAVEIZQ TKN_MAIN TKN_MAS TKN_MAYOR TKN_MAYORI TKN_MENOR TKN_MENORI TKN_MENOS TKN_MOD TKN_NEW TKN_NOT TKN_NULL TKN_OR TKN_PARDER TKN_PARIZQ TKN_POR TKN_POTENCIA TKN_PRINT TKN_PTCOMA TKN_PUNTO TKN_READ TKN_RETURN TKN_ROUND TKN_STRING TKN_SWITCH TKN_TOLOWER TKN_TO_UPPER TKN_TRUE TKN_TRUNCATE TKN_TYPE_OF TKN_VAR TKN_VOID TKN_WHILEs  :   instruccionesinstrucciones : instrucciones instruccioninstrucciones    : instruccion\n    finalizacion : TKN_PTCOMA\n                 | \n    \n    instruccion : instPrint finalizacion\n                | expresion finalizacion \n                | declararVar finalizacion\n                | asignacion finalizacion\n                | instIF\n    instPrint : TKN_PRINT TKN_PARIZQ expresion TKN_PARDER\n    expresion : expresion TKN_MAS expresion\n            | expresion TKN_MENOS expresion\n            | expresion TKN_POR expresion\n            | expresion TKN_DIV expresion\n            | expresion TKN_POTENCIA expresion\n            | expresion TKN_MOD expresion\n            | expresion TKN_IGUAL_IGUAL expresion\n            | expresion TKN_DIFERENTE expresion\n            | expresion TKN_MENOR expresion\n            | expresion TKN_MAYOR expresion\n            | expresion TKN_MENORI expresion\n            | expresion TKN_MAYORI expresion\n            | expresion TKN_OR expresion\n            | expresion TKN_AND expresion\n    \n    expresion : TKN_NOT expresion %prec UNOT\n    \n    expresion : TKN_MENOS expresion %prec UMENOS\n    \n    expresion : TKN_PARIZQ expresion TKN_PARDER\n    expresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : CHARACTERexpresion : TKN_FALSE\n                 | TKN_TRUE\n    expresion : TKN_NULLinstruccion        : error TKN_PTCOMAdeclararVar : TKN_VAR IDdeclararVar : TKN_VAR ID TKN_IGUAL expresionasignacion : ID TKN_IGUAL expresioninstIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDERinstIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER TKN_ELSE TKN_LLAVEIZQ instrucciones TKN_LLAVEDERinstIF : TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER instIF'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,75,76,77,79,80,81,82,],[9,9,-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,9,9,-41,-43,9,9,-42,]),'TKN_PRINT':([0,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,75,76,77,79,80,81,82,],[10,10,-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,10,10,-41,-43,10,10,-42,]),'TKN_NOT':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[13,13,-3,-5,-5,-5,-5,-10,13,13,13,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-8,-9,-37,13,-29,-27,-26,13,-38,13,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,13,-11,-39,13,13,-41,-43,13,13,-42,]),'TKN_MENOS':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,79,80,81,82,],[12,12,-3,-5,29,-5,-5,-10,12,12,12,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-8,-9,-37,12,29,-29,-27,-26,12,-38,12,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,29,-28,29,12,29,-11,29,12,12,-41,-43,12,12,-42,]),'TKN_PARIZQ':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[11,11,-3,-5,-5,-5,-5,-10,45,11,11,11,-29,-30,-31,-32,-33,-34,-35,-36,52,-2,-6,-4,-7,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-8,-9,-37,11,-29,-27,-26,11,-38,11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,11,-11,-39,11,11,-41,-43,11,11,-42,]),'ID':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[14,14,-3,-5,-5,-5,-5,-10,47,47,47,-29,-30,-31,-32,-33,-34,-35,-36,51,-2,-6,-4,-7,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-8,-9,-37,47,-29,-27,-26,47,-38,47,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,47,-11,-39,14,14,-41,-43,14,14,-42,]),'ENTERO':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[15,15,-3,-5,-5,-5,-5,-10,15,15,15,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-8,-9,-37,15,-29,-27,-26,15,-38,15,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,15,-11,-39,15,15,-41,-43,15,15,-42,]),'DECIMAL':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[16,16,-3,-5,-5,-5,-5,-10,16,16,16,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-8,-9,-37,16,-29,-27,-26,16,-38,16,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,16,-11,-39,16,16,-41,-43,16,16,-42,]),'CADENA':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[17,17,-3,-5,-5,-5,-5,-10,17,17,17,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-8,-9,-37,17,-29,-27,-26,17,-38,17,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,17,-11,-39,17,17,-41,-43,17,17,-42,]),'CHARACTER':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[18,18,-3,-5,-5,-5,-5,-10,18,18,18,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-8,-9,-37,18,-29,-27,-26,18,-38,18,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,18,-11,-39,18,18,-41,-43,18,18,-42,]),'TKN_FALSE':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[19,19,-3,-5,-5,-5,-5,-10,19,19,19,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-8,-9,-37,19,-29,-27,-26,19,-38,19,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,19,-11,-39,19,19,-41,-43,19,19,-42,]),'TKN_TRUE':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[20,20,-3,-5,-5,-5,-5,-10,20,20,20,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-8,-9,-37,20,-29,-27,-26,20,-38,20,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,20,-11,-39,20,20,-41,-43,20,20,-42,]),'TKN_NULL':([0,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,72,73,75,76,77,79,80,81,82,],[21,21,-3,-5,-5,-5,-5,-10,21,21,21,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-8,-9,-37,21,-29,-27,-26,21,-38,21,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,21,-11,-39,21,21,-41,-43,21,21,-42,]),'TKN_VAR':([0,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,75,76,77,79,80,81,82,],[22,22,-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,22,22,-41,-43,22,22,-42,]),'TKN_IF':([0,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,75,76,77,79,80,81,82,],[23,23,-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,23,23,23,-43,23,23,-42,]),'$end':([1,2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,77,79,82,],[0,-1,-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,-41,-43,-42,]),'TKN_LLAVEDER':([3,4,5,6,7,8,14,15,16,17,18,19,20,21,24,25,26,27,42,43,44,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,76,77,79,81,82,],[-3,-5,-5,-5,-5,-10,-29,-30,-31,-32,-33,-34,-35,-36,-2,-6,-4,-7,-8,-9,-37,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,77,-41,-43,82,-42,]),'TKN_PTCOMA':([4,5,6,7,9,14,15,16,17,18,19,20,21,47,48,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,72,73,],[26,26,26,26,44,-29,-30,-31,-32,-33,-34,-35,-36,-29,-27,-26,-38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-28,-40,-11,-39,]),'TKN_MAS':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[28,-29,-30,-31,-32,-33,-34,-35,-36,28,-29,-27,-26,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,28,-28,28,28,28,]),'TKN_POR':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[30,-29,-30,-31,-32,-33,-34,-35,-36,30,-29,-27,-26,30,30,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,30,-28,30,30,30,]),'TKN_DIV':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[31,-29,-30,-31,-32,-33,-34,-35,-36,31,-29,-27,-26,31,31,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,31,-28,31,31,31,]),'TKN_POTENCIA':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[32,-29,-30,-31,-32,-33,-34,-35,-36,32,-29,-27,-26,32,32,32,32,-16,32,-18,-19,-20,-21,-22,-23,-24,-25,32,-28,32,32,32,]),'TKN_MOD':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[33,-29,-30,-31,-32,-33,-34,-35,-36,33,-29,-27,-26,33,33,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,33,-28,33,33,33,]),'TKN_IGUAL_IGUAL':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[34,-29,-30,-31,-32,-33,-34,-35,-36,34,-29,34,34,34,34,34,34,34,34,-18,-19,-20,-21,-22,-23,34,34,34,-28,34,34,34,]),'TKN_DIFERENTE':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[35,-29,-30,-31,-32,-33,-34,-35,-36,35,-29,35,35,35,35,35,35,35,35,-18,-19,-20,-21,-22,-23,35,35,35,-28,35,35,35,]),'TKN_MENOR':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[36,-29,-30,-31,-32,-33,-34,-35,-36,36,-29,36,36,36,36,36,36,36,36,-18,-19,-20,-21,-22,-23,36,36,36,-28,36,36,36,]),'TKN_MAYOR':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[37,-29,-30,-31,-32,-33,-34,-35,-36,37,-29,37,37,37,37,37,37,37,37,-18,-19,-20,-21,-22,-23,37,37,37,-28,37,37,37,]),'TKN_MENORI':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[38,-29,-30,-31,-32,-33,-34,-35,-36,38,-29,38,38,38,38,38,38,38,38,-18,-19,-20,-21,-22,-23,38,38,38,-28,38,38,38,]),'TKN_MAYORI':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[39,-29,-30,-31,-32,-33,-34,-35,-36,39,-29,39,39,39,39,39,39,39,39,-18,-19,-20,-21,-22,-23,39,39,39,-28,39,39,39,]),'TKN_OR':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[40,-29,-30,-31,-32,-33,-34,-35,-36,40,-29,40,-26,40,40,40,40,40,40,-18,-19,-20,-21,-22,-23,-24,-25,40,-28,40,40,40,]),'TKN_AND':([5,14,15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,73,],[41,-29,-30,-31,-32,-33,-34,-35,-36,41,-29,41,-26,41,41,41,41,41,41,-18,-19,-20,-21,-22,-23,41,-25,41,-28,41,41,41,]),'TKN_IGUAL':([14,51,],[50,70,]),'TKN_PARDER':([15,16,17,18,19,20,21,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,],[-30,-31,-32,-33,-34,-35,-36,68,-29,-27,-26,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,72,-28,74,]),'TKN_LLAVEIZQ':([74,78,],[75,80,]),'TKN_ELSE':([77,],[78,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'instrucciones':([0,75,80,],[2,76,81,]),'instruccion':([0,2,75,76,80,81,],[3,24,3,24,3,24,]),'instPrint':([0,2,75,76,80,81,],[4,4,4,4,4,4,]),'expresion':([0,2,11,12,13,28,29,30,31,32,33,34,35,36,37,38,39,40,41,45,50,52,70,75,76,80,81,],[5,5,46,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,73,5,5,5,5,]),'declararVar':([0,2,75,76,80,81,],[6,6,6,6,6,6,]),'asignacion':([0,2,75,76,80,81,],[7,7,7,7,7,7,]),'instIF':([0,2,75,76,77,80,81,],[8,8,8,8,79,8,8,]),'finalizacion':([4,5,6,7,],[25,27,42,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> instrucciones','s',1,'p_s','gramatica.py',215),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','gramatica.py',219),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',226),
  ('finalizacion -> TKN_PTCOMA','finalizacion',1,'p_finalizacion','gramatica.py',234),
  ('finalizacion -> <empty>','finalizacion',0,'p_finalizacion','gramatica.py',235),
  ('instruccion -> instPrint finalizacion','instruccion',2,'p_instruccion','gramatica.py',242),
  ('instruccion -> expresion finalizacion','instruccion',2,'p_instruccion','gramatica.py',243),
  ('instruccion -> declararVar finalizacion','instruccion',2,'p_instruccion','gramatica.py',244),
  ('instruccion -> asignacion finalizacion','instruccion',2,'p_instruccion','gramatica.py',245),
  ('instruccion -> instIF','instruccion',1,'p_instruccion','gramatica.py',246),
  ('instPrint -> TKN_PRINT TKN_PARIZQ expresion TKN_PARDER','instPrint',4,'p_instPrint','gramatica.py',252),
  ('expresion -> expresion TKN_MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',258),
  ('expresion -> expresion TKN_MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',259),
  ('expresion -> expresion TKN_POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',260),
  ('expresion -> expresion TKN_DIV expresion','expresion',3,'p_expresion_binaria','gramatica.py',261),
  ('expresion -> expresion TKN_POTENCIA expresion','expresion',3,'p_expresion_binaria','gramatica.py',262),
  ('expresion -> expresion TKN_MOD expresion','expresion',3,'p_expresion_binaria','gramatica.py',263),
  ('expresion -> expresion TKN_IGUAL_IGUAL expresion','expresion',3,'p_expresion_binaria','gramatica.py',264),
  ('expresion -> expresion TKN_DIFERENTE expresion','expresion',3,'p_expresion_binaria','gramatica.py',265),
  ('expresion -> expresion TKN_MENOR expresion','expresion',3,'p_expresion_binaria','gramatica.py',266),
  ('expresion -> expresion TKN_MAYOR expresion','expresion',3,'p_expresion_binaria','gramatica.py',267),
  ('expresion -> expresion TKN_MENORI expresion','expresion',3,'p_expresion_binaria','gramatica.py',268),
  ('expresion -> expresion TKN_MAYORI expresion','expresion',3,'p_expresion_binaria','gramatica.py',269),
  ('expresion -> expresion TKN_OR expresion','expresion',3,'p_expresion_binaria','gramatica.py',270),
  ('expresion -> expresion TKN_AND expresion','expresion',3,'p_expresion_binaria','gramatica.py',271),
  ('expresion -> TKN_NOT expresion','expresion',2,'p_expresion_not','gramatica.py',308),
  ('expresion -> TKN_MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',314),
  ('expresion -> TKN_PARIZQ expresion TKN_PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',321),
  ('expresion -> ID','expresion',1,'p_expresion_ID','gramatica.py',327),
  ('expresion -> ENTERO','expresion',1,'p_expresion_ENTERO','gramatica.py',331),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_DECIMAL','gramatica.py',335),
  ('expresion -> CADENA','expresion',1,'p_expresion_CADENA','gramatica.py',339),
  ('expresion -> CHARACTER','expresion',1,'p_expresion_CHARACTER','gramatica.py',343),
  ('expresion -> TKN_FALSE','expresion',1,'p_expresion_boolean','gramatica.py',347),
  ('expresion -> TKN_TRUE','expresion',1,'p_expresion_boolean','gramatica.py',348),
  ('expresion -> TKN_NULL','expresion',1,'p_expresion_null','gramatica.py',353),
  ('instruccion -> error TKN_PTCOMA','instruccion',2,'p_instruccion_error','gramatica.py',357),
  ('declararVar -> TKN_VAR ID','declararVar',2,'p_declararVar','gramatica.py',364),
  ('declararVar -> TKN_VAR ID TKN_IGUAL expresion','declararVar',4,'p_declararVarAsignacion','gramatica.py',368),
  ('asignacion -> ID TKN_IGUAL expresion','asignacion',3,'p_asignacion','gramatica.py',374),
  ('instIF -> TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER','instIF',7,'p_instIF_simple','gramatica.py',380),
  ('instIF -> TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER TKN_ELSE TKN_LLAVEIZQ instrucciones TKN_LLAVEDER','instIF',11,'p_instIF_else','gramatica.py',384),
  ('instIF -> TKN_IF TKN_PARIZQ expresion TKN_PARDER TKN_LLAVEIZQ instrucciones TKN_LLAVEDER instIF','instIF',8,'p_instIF_elseIF','gramatica.py',388),
]
