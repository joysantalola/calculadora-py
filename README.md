# Calculadora en Python

Este es un programa simple de calculadora construido con Python y la biblioteca `tkinter` para crear una interfaz gráfica de usuario (GUI). El programa permite realizar operaciones matemáticas básicas como suma, resta, multiplicación, división, y también soporta el uso de decimales.

## Requisitos

Para ejecutar este programa, necesitas tener instalado lo siguiente:

- Python 3.x
- Tkinter (generalmente se incluye con Python, pero en algunas distribuciones de Linux puede ser necesario instalarlo por separado)

### Instalación

1. **Instalar Python 3.x**: Si aún no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Instalar Tkinter** (si no lo tienes instalado): Si usas una distribución de Linux, puedes instalar Tkinter ejecutando el siguiente comando en tu terminal:
    ```bash
    sudo apt-get install python3-tk
    ```

## Uso

1. Clona este repositorio o descarga los archivos a tu computadora.
2. Abre una terminal y navega al directorio donde descargaste el archivo.
3. Ejecuta el programa con el siguiente comando:
    ```bash
    python calculadora.py
    ```
4. Se abrirá una ventana con una interfaz gráfica en la que podrás hacer cálculos.

## Funcionalidades

- **Operaciones soportadas**:
  - Suma (`+`)
  - Resta (`-`)
  - Multiplicación (`*`)
  - División (`/`)
  - Punto decimal (`.`)
  - Borrado de la operación actual (`C`)
  - Igual (`=`) para obtener el resultado.

- **Interfaz de usuario**: La interfaz está compuesta por botones que permiten ingresar números y operaciones matemáticas.

- **Resultado**: El resultado se mostrará en la parte superior de la ventana. Si se introduce una operación inválida, se mostrará un mensaje de "Error".

## Captura de Pantalla

![Calculadora en Python](https://github.com/joysantalola/calculadora-py/blob/main/calc.png)

## Código

El programa se basa en una ventana `tkinter` que contiene botones para cada número y operación. La lógica detrás de cada operación está implementada en funciones que actualizan la pantalla de la calculadora.
