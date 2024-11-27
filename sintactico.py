import pytz
from datetime import datetime
import os
import ply.yacc as yacc

from lexico import tokens

result = 0

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
    | funcion 
    | if 
    | for'''

def p_asignacion(p):
  '''asignacion : VARIABLE ASSIGN expresion SEMICOLON'''

def p_print(p):
  '''print : ECHO datos SEMICOLON
  | ECHO SEMICOLON
  | ECHO argumentos SEMICOLON'''

def p_if(p):
  '''if : IF LPAREN operacionRelacional RPAREN LKEY NEWLINE programa RKEY
    | IF LPAREN operacionRelacional RPAREN LKEY NEWLINE programa RKEY ELSE LKEY NEWLINE programa RKEY NEWLINE'''

def p_for(p):
  '''for : FOR LPAREN VARIABLE ASSIGN datos SEMICOLON VARIABLE operadorRelacionalNumerico datos SEMICOLON operacionModificadoras RPAREN LKEY NEWLINE programa RKEY NEWLINE'''

def p_expresion(p):
  '''expresion : argumentos
    | FUNCTION_NAME LPAREN argumentos RPAREN
    | operacionAritmetica
    | operacionRelacional
    | readline
    | arregloIndexado
    | arregloDeclarado
    | operacionLogica
    | operadorLogico
    | ASSIGN_ADD
    | ASSIGN_SUB'''

def p_argumentos(p):
  '''argumentos : datos
    | datos COMMA argumentos'''
  
def p_datos(p):
  ''' datos : d_numericos
    | d_strings
    | d_booleanos
    | VARIABLE'''

def p_d_numericos(p):
  '''d_numericos : NUMBER
    | FLOAT'''

def p_d_strings(p):
  '''d_strings : STRING'''

def p_d_booleanos(p):
  '''d_booleanos : BOOLEAN'''

#REGLA SEMANTICA 1
def p_operacionAritmetica(p):
  '''operacionAritmetica : datos operadorAritmetico datos
  | datos operadorAritmetico operacionAritmetica'''
# 3 + 5

def p_operacionModificadoras(p):
  '''operacionModificadoras : VARIABLE INCREMENT
    | VARIABLE DECREMENT'''

def p_operacionLogica(p):
  '''operacionLogica : operacionRelacional operadorLogico operacionRelacional
  | operacionRelacional operadorLogico operacionLogica
  | '''
# true && true

def p_operacionRelacional(p):
  '''operacionRelacional : operacionRelacionalGeneral
  | operacionRelacionalNumerica'''

def p_operacionRelacionalGeneral(p):
  '''operacionRelacionalGeneral : VARIABLE operadorRelacionalGeneral datos'''

#REGLA SEMANTICA 2
def p_operacionRelacionalNumerica(p):
  '''operacionRelacionalNumerica : VARIABLE operadorRelacionalNumerico d_numericos'''

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

def p_funcion(p):
  '''funcion : FUNCTION FUNCTION_NAME LPAREN datos_comma RPAREN LKEY NEWLINE cuerpoFuncion RKEY 
  | FUNCTION FUNCTION_NAME LPAREN RPAREN LKEY NEWLINE cuerpoFuncion RKEY'''

def p_datos_comma(p):
  '''datos_comma : datos
    | datos COMMA datos_comma'''

def p_cuerpoFuncion(p):
  '''cuerpoFuncion : programa RETURN expresion SEMICOLON NEWLINE
  | programa
  | RETURN expresion SEMICOLON NEWLINE'''

def p_readline(p):
  '''readline : READLINE LPAREN RPAREN'''

# Error rule for syntax errors
def p_error(p):
    global result
    if p:
      mensaje = f"Error de sintaxis en la línea {p.lineno}: Token inesperado '{p.value}'"
      
    else:
      mensaje = "Error de sintaxis: Fin de entrada inesperado"      
    print(mensaje)
    result += 1
    exit()
    
# Build the parser
parser = yacc.yacc()


# #CREACIÓN DE LOGS
# zona_horaria = pytz.timezone("America/Guayaquil")
# fecha_actual = datetime.now(zona_horaria)
# usuario = "katherineforero"  #se va cambiando el nombre del usuario según el caso
# fecha_act = fecha_actual.strftime("%d%m%Y-%Hh%M")
# os.makedirs("logs_sintactico", exist_ok=True)
# nombre = "sintactico-" + usuario + "-" + fecha_act + ".txt"

# ruta_archivo = os.path.join("logs_sintactico", nombre)
# with open(ruta_archivo, "w") as archivo:  
#       if errores_sintacticos:
#         archivo.write("Errores de sintaxis detectados:\n")
#         archivo.write("\n".join(errores_sintacticos) + "\n")
#       else:
#         archivo.write(str(result) + "\n")