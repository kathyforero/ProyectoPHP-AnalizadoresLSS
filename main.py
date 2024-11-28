import os
from lexico import tokens  # Asegúrate de tener el archivo lexico.py y el token correctamente configurado
import ply.yacc as yacc
from sintactico import parser  # Importa el parser desde tu archivo de análisis (el archivo donde definiste el parser)
from sintactico import parser as parser_sintactico
from semantico import parser as parser_semantico


dato2 = """
$a -= 2;
"""

result = parser_sintactico.parse(dato2)
result = parser_semantico.parse(dato2)  # Llama al parser para analizar los datos

