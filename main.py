import os
from lexico import tokens  # Asegúrate de tener el archivo lexico.py y el token correctamente configurado
import ply.yacc as yacc
from sintactico import parser  # Importa el parser desde tu archivo de análisis (el archivo donde definiste el parser)
from sintactico import parser as parser_sintactico
from semantico import parser as parser_semantico
# from build.gui import *
import tkinter as tk


# def configurar_run():
#     dato = entry_1.get("1.0", "end-1c")
#     print(dato)
#
#     entry_2.config(state="normal")  # Habilitar para modificar
#     entry_2.delete("1.0", "end")  # Limpiar el contenido
#     entry_2.insert("1.0", dato)  # Insertar el texto extraído
#     entry_2.config(state="disabled")  # Deshabilitar el widget después de modificarlo
#     result = parser_sintactico.parse(dato)
#     result = parser_semantico.parse(dato)  # Llama al parser para analizar los datos
#
# def cerrar_ventana(window):
#     window.quit()  # Termina el ciclo de eventos de Tkinter y cierra la ventana
#
def main():
    # Crea una instancia de Tkinter
    window = tk.Tk()

    # Ejecutamos la ventana de GUI
    window.mainloop()

if __name__ == "__main__":
    main()

