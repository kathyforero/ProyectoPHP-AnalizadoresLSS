import pytz
from datetime import datetime
import os
import ply.yacc as yacc

from lexico import tokens

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
  '''for : FOR LPAREN VARIABLE ASSIGNATION programa SEMICOLON VARIABLE operadorRelacional datos SEMICOLON operacionModificadoras RPAREN '''

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
    | datos conector argumentos'''

def p_conector(p):
  '''conector : COMMA
    | PERIOD'''

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
  
def p_operacionAritmetica(p):
  '''operacionAritmetica : datos operadorAritmetico datos
  | datos operadorAritmetico operacionAritmetica'''
# 3 + 5

def p_operacionModificadoras(p):
  '''operacionModificadoras : VARIABLE INCREMENT
    | VARIABLE DECREMENT'''

def p_operacionLogica(p):
  '''operacionLogica : operacionRelacional operadorLogico operacionRelacional
  | operacionRelacional operadorLogico operacionLogica'''
# true && true

def p_operacionRelacional(p):
  '''operacionRelacional : datos operadorRelacional datos'''


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
  
def p_operadorRelacional(p):
  ''' operadorRelacional : GREATER
  | LESS
  | EQUALS
  | DIFFERENT
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
  '''funcion : FUNCTION FUNCTION_NAME LPAREN datos_comma RPAREN LKEY NEWLINE cuerpoFuncion RKEY'''

def p_datos_comma(p):
  '''datos_comma : datos
    | datos COMMA datos_comma'''

def p_cuerpoFuncion(p):
  '''cuerpoFuncion : programa RETURN expresion SEMICOLON
  | programa
  | RETURN expresion SEMICOLON'''

def p_readline(p):
  '''readline : READLINE LPAREN STRING RPAREN'''

# Error rule for syntax errors
errores_sintacticos = []
def p_error(p):
    if p:
      mensaje = f"Error de sintaxis en la línea {p.lineno}: Token inesperado '{p.value}'"
    else:
      mensaje = "Error de sintaxis: Fin de entrada inesperado"
    print(mensaje)
    errores_sintacticos.append(mensaje)

# Build the parser
parser = yacc.yacc()

dato = """
$num1 = 10;
$num2 = 5;

function operaciones($a, $b) {
     // Calcular cada operación
    $suma = $a + $b;
    $resta = $a - $b;
    $multiplicacion = $a * $b;

    // Usar un 'if' para verificar la división por cero
    if ($b != 0) {
        $division = $a / $b;
    } else {
        $division = 'No se puede dividir por cero';
    }

    // Devolver los resultados en un array
    return [
        "suma" => $suma,
        "resta" => $resta,
        "multiplicacion" => $multiplicacion,
        "division" => $division
    ];
    }"""

dato2 = """
// Array asociativo de frutas con su precio unitario
$frutas = [
    "manzana" => 2.5,
    "banana" => 1.8,
    "naranja" => 3.0,
    "pera" => 2.2,
    "uva" => 4.0
];

// Función para calcular el total a pagar
function calcularTotal($nombreFruta, $cantidad, $arregloFrutas) {
    // Verificar si la fruta existe en el arreglo
    if ($cantidad > 5) {
        // Calcular el total
        $precioUnitario = $arregloFrutas;
        $total = $precioUnitario * $cantidad;
        $retorno = $total;
    } else {        
        $retorno = "La fruta no esta disponible";
    }
    return "$retorno";}"""
# Pasar todo el contenido directamente al analizador
print("Probando el programa completo:")
result = parser.parse(dato2)
print(result)

#CREACIÓN DE LOGS
zona_horaria = pytz.timezone("America/Guayaquil")
fecha_actual = datetime.now(zona_horaria)
usuario = "katherineforero"  #se va cambiando el nombre del usuario según el caso
fecha_act = fecha_actual.strftime("%d%m%Y-%Hh%M")
os.makedirs("logs_sintactico", exist_ok=True)
nombre = "sintactico-" + usuario + "-" + fecha_act + ".txt"

ruta_archivo = os.path.join("logs_sintactico", nombre)
with open(ruta_archivo, "w") as archivo:  
      if errores_sintacticos:
        archivo.write("Errores de sintaxis detectados:\n")
        archivo.write("\n".join(errores_sintacticos) + "\n")
      else:
        archivo.write(str(result) + "\n")