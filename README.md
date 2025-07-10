


# README - Analizador de Lenguaje PHP

## Descripción

Este proyecto es un **analizador de lenguaje PHP** que implementa las tres fases clásicas del front-end de un compilador: análisis léxico, análisis sintáctico y análisis semántico. [1](#0-0) [2](#0-1) [3](#0-2) 

El sistema está diseñado con fines educativos para demostrar los conceptos fundamentales de compiladores y procesamiento de lenguajes. Incluye una interfaz gráfica de usuario intuitiva que permite analizar código PHP en tiempo real con retroalimentación visual de errores.

## Características Principales

### 🔍 **Análisis Completo en Tres Fases**
- **Análisis Léxico**: Tokenización de código PHP con manejo de variables, operadores, palabras clave y literales [4](#0-3) 
- **Análisis Sintáctico**: Construcción de árbol de sintaxis abstracta usando gramática LALR [5](#0-4) 
- **Análisis Semántico**: Validación de tipos y manejo de tablas de símbolos [6](#0-5) 

### 🖥️ **Interfaz Gráfica Intuitiva**
- Editor de código integrado para entrada de código PHP
- Visualización de resultados con codificación de colores para errores
- Interfaz construida con tkinter para máxima compatibilidad [7](#0-6) 

### ⚠️ **Sistema de Gestión de Errores**
- Detección y reporte de errores en las tres fases de análisis
- Mensajes de error descriptivos con formato de color:
  - **Errores léxicos**: Caracteres ilegales [8](#0-7) 
  - **Errores sintácticos**: Violaciones de gramática [9](#0-8) 
  - **Errores semánticos**: Variables no declaradas, funciones indefinidas, incompatibilidades de tipos [10](#0-9) 

### 📊 **Tablas de Símbolos**
- Seguimiento en tiempo real de variables declaradas
- Registro de funciones definidas
- Validación de existencia de símbolos antes de uso [11](#0-10) 

## Arquitectura del Sistema

El proyecto sigue una arquitectura modular de front-end de compilador con separación clara de responsabilidades:

```
Pipeline de Procesamiento de Lenguaje
├── Entrada de Código PHP
├── Análisis Léxico (lexico.py)
├── Análisis Sintáctico (sintactico.py) 
├── Análisis Semántico (semantico.py)
└── Resultados y Errores
```

### Componentes Principales

| Componente | Archivo | Función |
|------------|---------|---------|
| **Controlador Principal** | `main.py` | Orquesta las fases de análisis [12](#0-11)  |
| **Interfaz Gráfica** | `GUI/gui.py` | Proporciona la interfaz de usuario [13](#0-12)  |
| **Analizador Léxico** | `lexico.py` | Tokenización de código fuente |
| **Analizador Sintáctico** | `sintactico.py` | Construcción de AST |
| **Analizador Semántico** | `semantico.py` | Validación semántica |
| **Tablas de Parser** | `parsetab.py` | Tablas LALR generadas automáticamente [14](#0-13)  |

## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **PLY (Python Lex-Yacc)**: Framework para generación de analizadores léxicos y sintácticos [15](#0-14) 
- **tkinter**: Biblioteca para la interfaz gráfica de usuario
- **Algoritmo LALR**: Para análisis sintáctico eficiente [16](#0-15) 

## Instalación y Requisitos

### Requisitos del Sistema
- Python 3.6 o superior
- PLY (Python Lex-Yacc)
- tkinter (incluido en la mayoría de instalaciones de Python)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/kathyforero/ProyectoPHP-AnalizadoresLSS.git

# Navegar al directorio del proyecto
cd ProyectoPHP-AnalizadoresLSS

# Instalar dependencias
pip install ply
```

## Uso

### Ejecutar la Aplicación
```bash
# Ejecutar la interfaz gráfica
python GUI/gui.py

# O ejecutar el controlador principal
python main.py
```

### Cómo Usar el Analizador

1. **Ejecutar la aplicación** para abrir la interfaz gráfica
2. **Escribir o pegar código PHP** en el área de entrada de texto
3. **Hacer clic en "Analizar"** para procesar el código
4. **Revisar los resultados** en el área de salida:
   - **Texto verde**: Análisis exitoso
   - **Texto rojo**: Errores detectados con descripción detallada
   - **Tablas de símbolos**: Variables y funciones detectadas

### Reglas Semánticas Soportadas

El analizador implementa cinco reglas semánticas principales: [17](#0-16) 

1. **Operaciones Aritméticas**: Validación de tipos en operaciones numéricas
2. **Operaciones Relacionales**: Verificación de tipos en comparaciones
3. **Existencia de Variables**: Comprobación de declaración antes del uso [18](#0-17) 
4. **Existencia de Funciones**: Validación de funciones definidas antes de invocación
5. **Acumulación Numérica**: Verificación de operaciones de incremento/decremento

## Estructura del Proyecto

```
ProyectoPHP-AnalizadoresLSS/
├── GUI/
│   └── gui.py              # Interfaz gráfica de usuario
├── logs/                   # Archivos de registro de análisis
├── lexico.py              # Analizador léxico
├── main.py                # Controlador principal
├── parser.out             # Estados de gramática generados
├── parsetab.py           # Tablas de parser LALR
├── semantico.py          # Analizador semántico
├── sintactico.py         # Analizador sintáctico
└── uv.lock              # Archivo de dependencias
```

## Características Educativas

Este proyecto está diseñado específicamente para fines educativos e incluye:

- **Implementación clara** de cada fase de análisis
- **Comentarios detallados** en el código fuente
- **Manejo comprensivo de errores** con mensajes informativos
- **Visualización de tablas de símbolos** para comprensión del proceso
- **Ejemplos de algoritmos** para testing

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Autores

- **Kathy Forero** - Desarrollo principal

## Licencia

Este proyecto tiene fines educativos y está disponible para uso académico y de aprendizaje.

---

## Notas

Este README proporciona una guía completa para entender, instalar y usar el Analizador de Lenguaje PHP. El proyecto demuestra conceptos fundamentales de compiladores de manera práctica y accesible, siendo una excelente herramienta para estudiantes y educadores en ciencias de la computación.
