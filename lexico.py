import sys

import pytz
import ply.lex as lex
from datetime import datetime
import os

# List of token names. This is always required

errores = []

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
          'COMMA', 
          'LCOR',
          'RCOR', 
          'ECHO', 
          'IF', 
          'ELSE',
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
          'FOR', 
          'INCREMENT',
          'DECREMENT', 
          'FUNCTION', 
          'FUNCTION_NAME', 
          'RETURN', 
          'COMMENT1',
          'DIFFERENT',
          'COUNT',
          'GREATER',
          'LESS',
          'EQUALS',
          'GREATER_EQUALS',
          'LESS_EQUALS',
          'READLINE',
          'PERIOD',
          'NEWLINE'
    )

states = (
    ('funcname', 'exclusive'),  # Estado exclusivo para nombres de funciones
)

# Inicio aporte: David Ramírez
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
t_PERIOD = r'\.'
# A regular expression rule with some action code


#COMENTARIOS
def t_COMMENT1(t):
    r'//.*|\#.*'
    pass

# Fin aporte: David Ramírez

#PALABRAS RESERVADAS

# Inicio aporte: Katherine Forero
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


# Fin aporte: Katherine Forero

# Inicio aporte: David Ramírez

def t_RETURN(t):
    r'(r|R)(e|E)(t|T)(u|U)(r|R)(n|N)'
    return t

def t_ASSIGNATION(t):
    r'=>'
    return t

def t_FUNCTION(t):
    r'\bfunction\b'
    t.lexer.begin('funcname')  # Cambia al estado 'funcname' al encontrar 'function'
    return t

def t_funcname_FUNCTION_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'FUNCTION_NAME'
    t.lexer.begin('INITIAL')  # Vuelve al estado inicial después de encontrar el nombre de la función
    return t

def t_READLINE(t):
    r'(r|R)(e|E)(a|A)(d|D)(l|L)(i|I)(n|N)(e|E)'
    return t 

# Fin aporte: David Ramírez

# Inicio aporte: Katherine Forero

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

# Fin aporte: Katherine Forero

# Inicio aporte: David Ramírez

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

# Fin aporte: David Ramírez

# Inicio aporte: Katherine Forero

#TIPOS DE DATOS
def t_FLOAT(t):
    r'(\-)?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_BOOLEAN(t):
    r'(t|T)(r|R)(u|U)(e|E)|(f|F)(a|A)(l|L)(s|S)(e|E)'
    return t


def t_NUMBER(t):
    r'(\-)?\d+'
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
   return t

# NOMBRE DE FUNCIÓN FUERA DE RESTRICCIONES

def t_FUNCTION_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Fin aporte: Katherine Forero

#IGNORE
t_ignore = ' \t'

t_funcname_ignore = ' \t'

#ERROR
def t_error(t):
    global errores
    print("Error Léxico: Caracter ilegal '%s'" % t.value[0])
    errores.append("Error Léxico: Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Manejo de errores en el estado 'funcname'
def t_funcname_error(t):
    print(f"Error Léxico: Caracter ilegal '{t.value[0]}'")
    errores.append(f"Error Léxico: Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

#Construir el Lex
lexer = lex.lex()

