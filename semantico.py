import pytz
from datetime import datetime
import os
import ply.yacc as yacc

from lexico import tokens

errores3 = []

def p_programa(p):
  '''programa : bloque
     | bloque programa
     | comment bloque programa'''

def p_comment(p):
  '''comment : COMMENT1
    | COMMENT1 NEWLINE'''
  pass

def p_bloque(p):
  '''bloque : sentencia NEWLINE
    | sentencia
    | NEWLINE'''

def p_sentencia(p):
  '''sentencia : print
    | asignacion
    | variable
    | funcion 
    | if 
    | for
    | invocar
    | operacionModificadoras SEMICOLON'''



##################################################################################################
# REGLA SEMÁNTICA 3
#VERIFICAR QUE LAS VARIABLES EXISTAN AL IMPRIMIR
variables_existentes = set()
funciones_existentes = set()

def p_asignacion(p):
  '''asignacion : VARIABLE ASSIGN expresion SEMICOLON'''
  var_name = p[1]
  variables_existentes.add(var_name)



########################################################################################################
# REGLA SEMÁNTICA 5
#INCREMENTAR Y DECREMENTAR VARIABLES NUMÉRICAS 
def p_variable_incremento_decremento(p):
  '''variable : VARIABLE ASSIGN_ADD d_numericos SEMICOLON
  | VARIABLE ASSIGN_SUB d_numericos SEMICOLON'''

def p_variable_incremento_decremento_error(p):
  '''variable : VARIABLE ASSIGN_ADD error SEMICOLON
  | VARIABLE ASSIGN_SUB error SEMICOLON'''
  print("Error semántico: Se ha encontrado un error. Para acumular solo se permiten datos numéricos.")
  errores3.append("Error semántico: Se ha encontrado un error. Para acumular solo se permiten datos numéricos.")

def p_print(p):
  '''print : ECHO datos SEMICOLON
  | ECHO SEMICOLON
  | ECHO argumentos SEMICOLON'''

def p_if(p):
  '''if : IF LPAREN operacionRelacional RPAREN LKEY NEWLINE programa RKEY
    | IF LPAREN operacionRelacional RPAREN LKEY NEWLINE programa RKEY ELSE LKEY NEWLINE programa RKEY NEWLINE'''

def p_for(p):
  '''for : FOR LPAREN asignacion VARIABLE operadorRelacionalNumerico datos SEMICOLON operacionModificadoras RPAREN LKEY NEWLINE programa RKEY NEWLINE'''

def p_expresion(p):
  '''expresion : argumentos
    | invocar
    | operacionAritmetica
    | operacionRelacional
    | readline
    | arregloIndexado
    | arregloDeclarado
    | operacionLogica
    | operadorLogico
  '''

###################################################################################
# REGLA SEMÁNTICA 3 (CONTINUACIÓN)

def p_argumentos_multiple(p):
  '''argumentos : datos COMMA argumentos'''

def p_argumentos_single(p):
  '''argumentos : datos'''
  p[0] = p[1]

def p_datos_variable(p):
  '''datos : VARIABLE'''
  var_name = p[1]
  if var_name not in variables_existentes:
    print(f"Error semántico: Variable '{var_name}' no ha sido declarada.")
    errores3.append(f"Error semántico: Variable '{var_name}' no ha sido declarada.")
  p[0] = var_name


def p_datos_string(p):
  '''datos : d_strings'''
  p[0] = p[1]


def p_datos_number(p):
  '''datos : d_numericos'''
  p[0] = str(p[1])


def p_datos_boolean(p):
  '''datos : d_booleanos'''
  p[0] = p[1]


def p_d_numericos(p):
  '''d_numericos : NUMBER
    | FLOAT'''

def p_d_strings(p):
  '''d_strings : STRING'''

def p_d_booleanos(p):
  '''d_booleanos : BOOLEAN'''

def p_argumentos_funcion(p):
  '''argumentosFuncion : argumentoFuncion
  | argumentoFuncion argumentosFuncion'''

def p_argumento_funcion_variable(p):
  '''argumentoFuncion : VARIABLE'''
  var_name = p[1]
  variables_existentes.add(var_name)

def p_argumento_funcion_string(p):
  '''argumentoFuncion : d_strings'''
  p[0] = p[1]


def p_argumento_funcion_number(p):
  '''argumentoFuncion : d_numericos'''
  p[0] = str(p[1])

def p_argumento_funcion_boolean(p):
  '''argumentoFuncion : d_booleanos'''
  p[0] = p[1]

# REGLA SEMÁNTICA 4
#VALIDAR FUNCIONES EXISTENTES PARA SU INVOCACIÓN DENTRO DEL CODIGO

def p_invocar_funcion(p):
  '''invocar : FUNCTION_NAME LPAREN datos_comma RPAREN SEMICOLON
  | FUNCTION_NAME LPAREN RPAREN SEMICOLON'''
  fun_name = p[1]
  if fun_name not in funciones_existentes:
    print(f"Error semántico: Función '{fun_name}' no ha sido creada.")
    errores3.append(f"Error semántico: Función '{fun_name}' no ha sido creada.")

def p_funcion(p):
  '''funcion : FUNCTION FUNCTION_NAME LPAREN argumentosFuncion RPAREN LKEY NEWLINE cuerpoFuncion RKEY
  | FUNCTION FUNCTION_NAME LPAREN RPAREN LKEY NEWLINE cuerpoFuncion RKEY'''
  fun_name = p[2]
  funciones_existentes.add(fun_name)

def p_datos_comma(p):
  '''datos_comma : datos
    | datos COMMA datos_comma'''

def p_cuerpoFuncion(p):
  '''cuerpoFuncion : programa RETURN expresion SEMICOLON NEWLINE
  | programa
  | RETURN expresion SEMICOLON NEWLINE'''

##########################################################################
# REGLA SEMÁNTICA 1
#REGLA PARA EXPRESIONES ARI TMÉTICAS SOLOS PARA DATOS NUMÉRICOS
def p_operacionAritmetica(p):
  '''operacionAritmetica : d_numericos operadorAritmetico d_numericos
  | VARIABLE operadorAritmetico d_numericos
  | d_numericos operadorAritmetico VARIABLE
  | VARIABLE operadorAritmetico VARIABLE
  | d_numericos operadorAritmetico operacionAritmetica'''
# 3 + 5

def p_operacionAritmetica_error(p):
  '''operacionAritmetica : error operadorAritmetico error'''
  print("Error semántico: Se ha encontrado un error en la expresión aritmética. Operación incorrecta.")
  errores3.append("Error semántico: Se ha encontrado un error en la expresión aritmética. Operación incorrecta.")


def p_operacionModificadoras(p):
  '''operacionModificadoras : VARIABLE INCREMENT
    | VARIABLE DECREMENT'''

def p_operacionLogica(p):
  '''operacionLogica : operacionRelacional operadorLogico operacionRelacional
  | operacionRelacional operadorLogico operacionLogica
  | '''

def p_operacionRelacional(p):
  '''operacionRelacional : operacionRelacionalGeneral
  | operacionRelacionalNumerica'''

def p_operacionRelacionalGeneral(p):
  '''operacionRelacionalGeneral : datos operadorRelacionalGeneral datos'''


###################################################################
#REGLA SEMÁNTICA 2
#OPERACION PARA COMPARAR UN DATO (¡PHP PASA LOS STRING A 0 CUANDO COMPARA!) CON UN NÚMERO
def p_operacionRelacionalNumerica(p):
  '''operacionRelacionalNumerica : datos operadorRelacionalNumerico d_numericos
  | datos operadorRelacionalNumerico VARIABLE'''

def p_operacionRelacionalNumerica_error(p):
  '''operacionRelacionalNumerica : datos operadorRelacionalNumerico error'''
  print("Error semántico: Se ha encontrado un error en la expresión relacional. El segundo objeto de la comparación debe ser numérico.")
  errores3.append("Error semántico: Se ha encontrado un error en la expresión relacional. El segundo objeto de la comparación debe ser numérico.")


def p_operadorAritmetico(p):
  ''' operadorAritmetico : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD '''

def p_operadorLogico(p):
  ''' operadorLogico : LOGICAL_AND
    | LOGICAL_OR
    | LOGICAL_NOT 
    '''

def p_operadorRelacionalGeneral(p):
  ''' operadorRelacionalGeneral : EQUALS
  | DIFFERENT'''

def p_operadorRelacionalNumerico(p):
  ''' operadorRelacionalNumerico : GREATER
  | LESS
  | GREATER_EQUALS
  | LESS_EQUALS'''

def p_arregloDeclarado(p):
  '''arregloDeclarado : LCOR NEWLINE cuerpoArregloDeclarado NEWLINE RCOR'''

def p_cuerpoArregloDeclarado(p):
  '''cuerpoArregloDeclarado : datos ASSIGNATION datos
  | datos ASSIGNATION datos COMMA NEWLINE cuerpoArregloDeclarado'''

def p_arregloIndexado(p):
  '''arregloIndexado : LCOR datos_comma RCOR'''

def p_readline(p):
  '''readline : READLINE LPAREN RPAREN'''

# Error rule for syntax errors
def p_error(p):
  ""

parser = yacc.yacc()