import pytz
import ply.lex as lex
from datetime import datetime
import os

# List of token names. This is always required
tokens = ('NUMBER', 
          'PLUS', 
          'MINUS', 
          'TIMES', 
          'DIVIDE', 
          'LPAREN', 
          'RPAREN',
          'MOD', 
          'VARIABLE', 
          'SEMICOLON', 
          'FLOAT', 
          'PRINT', 
          'COMMA', 
          'LCOR',
          'RCOR', 
          'ECHO', 
          'IF', 
          'ELSE',
          'ELSEIF',
          'STRING', 
          'BOOLEAN', 
          'ASSIGNATION',
          'LOGICAL_AND', 
          'LOGICAL_OR', 
          'LOGICAL_NOT', 
          'ASSIGN', 
          'ASSIGN_ADD',
          'ASSIGN_SUB', 
          'LKEY', 
          'RKEY', 
          'BREAK', 
          'FOR', 
          'INCREMENT',
          'DECREMENT', 
          'FUNCTION', 
          'RETURN', 
          'COMMENT1', 
          'COMMENT2',
          'DIFFERENT',
          'COUNT',
          'GREATER',
          'LESS',
          'EQUALS',
          'GREATER_EQUALS',
          'LESS_EQUALS',
          'READLINE',
          'TRIM'
    )

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCOR = r'\['
t_RCOR = r'\]'
t_LKEY = r'{'
t_RKEY = r'}'
t_MOD = r'\%'
t_SEMICOLON = r';'
t_COMMA = r','

# A regular expression rule with some action code


#COMENTARIOS
def t_COMMENT1(t):
    r'//.*'
    pass

def t_COMMENT2(t):
    r'//.*'
    pass

#PALABRAS RESERVADAS
def t_IF(t):
    r'(i|I)(f|F)'
    return t

def t_ELSE(t):
    r'(E|e)(L|l)(S|s)(E|e)'
    return t

def t_FOR(t):
    r'(F|f)(O|o)(R|r)'
    return t

def t_ECHO(t):
    r'(e|E)(c|C)(h|H)(o|O)'
    return t


def t_ELSEIF(t):
    r'(e|E)(l|L)(s|S)(e|E)(i|I)(f|F)'
    return t


def t_BREAK(t):
    r'(b|B)(r|R)(e|E)(a|A)(k|K)'
    return t


def t_RETURN(t):
    r'(r|R)(e|E)(t|T)(u|U)(r|R)(n|N)'
    return t

def t_ASSIGNATION(t):
    r'=>'
    return t

def t_FUNCTION(t):
    r'\bfunction\s+[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value.strip()
    return t

def t_COUNT(t):
    r'(c|C)(o|O)(u|U)(n|N)(t|T)'
    return t

def t_READLINE(t):
    r'(r|R)(e|E)(a|A)(d|D)(l|L)(i|I)(n|N)(e|E)'
    return t

def t_TRIM(t):
    r'(t|T)(r|R)(i|I)(m|M)'
    return t   

#OPERADORES LOGICOS
def t_GREATER_EQUALS(t):
    r'>='
    return t

def t_LESS_EQUALS(t):
    r'<='
    return t

def t_GREATER(t):
    r'>'
    return t

def t_LESS(t):
    r'<'
    return t

def t_EQUALS(t):
    r'=='
    return t

def t_DIFFERENT(t):
    r'!='
    return t

def t_LOGICAL_AND(t):
    r'&&'
    return t


def t_LOGICAL_OR(t):
    r'\|\|'
    return t


def t_LOGICAL_NOT(t):
    r'!'
    return t


def t_ASSIGN(t):
    r'='
    return t


def t_ASSIGN_ADD(t):
    r'\+='
    return t


def t_ASSIGN_SUB(t):
    r'-='
    return t


def t_INCREMENT(t):
    r'\+\+'
    return t


def t_DECREMENT(t):
    r'--'
    return t


#TIPOS DE DATOS
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_BOOLEAN(t):
    r'(t|T)(r|R)(u|U)(e|E)|(f|F)(a|A)(l|L)(s|S)(e|E)'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"(\".*?\"|\'.*?\')"
    t.value = t.value[1:-1]
    return t


def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#IGNORE
t_ignore = ' \t'


#ERROR
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#Construir el Lex
lexer = lex.lex()

# Test it out
data1 = '''
// Definir las dos variables
$num1 = 10;
$num2 = 5;

// Función que realiza las operaciones
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
}
'''

data2 = '''
// Definir el arreglo indexado
$numeros = [10, 20, 30, 40, 50];

// Función para sumar los elementos del arreglo usando un bucle for
function sumaElementos($arr) {
    // Inicializar la suma
    $suma = 0;

    // Recorrer el arreglo usando un bucle for
    for ($i = 0; $i < count($arr); $i++) {
        $suma += $arr[$i];  // Sumar cada elemento
    }

    // Devolver el resultado
    return $suma;
}
'''


data3 = '''
$Dato = trim(readline("Ingrese un dato: "));
echo $Dato;
'''

# Give the lexer some input
lexer.input(data3)

#CREACIÓN DE LOGS
zona_horaria = pytz.timezone("America/Guayaquil")
fecha_actual = datetime.now(zona_horaria)
usuario = "DERS0214"  #se va cambiando el nombre del usuario según el caso
algoritmo = "ALG3"
fecha_act = fecha_actual.strftime("%d%m%Y-%Hh%M")
os.makedirs("logs", exist_ok=True)
nombre = algoritmo + "-lexico-" + usuario + "-" + fecha_act + ".txt"

ruta_archivo = os.path.join("logs", nombre)
with open(ruta_archivo, "w") as archivo:
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        archivo.write(str(tok) + "\n")
