"""
Practica 4
Archivo Instrucciones
"""

import turtle
import os

# Configuracion de ventana
screen = turtle.Screen()
screen.title("Practica 4 - Archivo Instrucciones")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Funciones base de dibujo
def dibujar_cuadrado(x, y, lado, color):
    """
    Dibuja un cuadrado en la posicion (x, y).
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(lado)
        t.right(90)
    t.penup()

def dibujar_triangulo(x, y, lado, color):
    """
    Dibuja un triangulo equilatero en la posicion (x, y).
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(3):
        t.forward(lado)
        t.left(120)
    t.penup()

def dibujar_circulo(x, y, radio, color):
    """
    Dibuja un circulo aproximado con pasos de 1 grado.
    """
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(color)
    for _ in range(360):
        t.forward(2 * 3.1416 * radio / 360)
        t.left(1)
    t.penup()

def dibujar_linea(x1, y1, x2, y2, color):
    """
    Dibuja una linea recta entre dos puntos.
    """
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.goto(x2, y2)
    t.penup()

def teleport(x, y):
    """
    Mueve la tortuga a una coordenada sin dibujar.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

# Lectura de archivo de instrucciones
def leer_instrucciones():
    """
    Lee el archivo dibujante.txt y devuelve una lista con las instrucciones.
    """
    base = os.path.dirname(__file__)
    filename = os.path.join(base, "dibujante.txt")  # otra vez "os" por el VSCode

    instrucciones = []
    for line in open(filename, encoding="utf-8"):
        if line.strip():   # ignorar lineas vacias
            instrucciones.append(line.strip())
    return instrucciones

# Ejecucion de instrucciones
def ejecutar_instrucciones(instrucciones):
    """
    Ejecuta las instrucciones leidas del archivo.
    """
    for num_linea, linea in enumerate(instrucciones, start=1):  # enumerate() nos da el numero de linea
        partes = linea.split()  # separa la linea en palabras
        instruccion = partes[0].upper()

        try:
            if instruccion == "CUADRADO":
                # CUADRADO x y lado color
                x, y, lado, color = partes[1], partes[2], partes[3], partes[4]
                dibujar_cuadrado(float(x), float(y), float(lado), color)

            elif instruccion == "TRIANGULO":
                # TRIANGULO x y lado color
                x, y, lado, color = partes[1], partes[2], partes[3], partes[4]
                dibujar_triangulo(float(x), float(y), float(lado), color)

            elif instruccion == "CIRCULO":
                # CIRCULO x y radio color
                x, y, radio, color = partes[1], partes[2], partes[3], partes[4]
                dibujar_circulo(float(x), float(y), float(radio), color)

            elif instruccion == "LINEA":
                # LINEA x1 y1 x2 y2 color
                x1, y1, x2, y2, color = partes[1], partes[2], partes[3], partes[4], partes[5]
                dibujar_linea(float(x1), float(y1), float(x2), float(y2), color)

            elif instruccion == "TELEPORT":
                # TELEPORT x y
                x, y = partes[1], partes[2]
                teleport(float(x), float(y))

            else:
                print(f"[ERROR] Linea {num_linea}: Instruccion desconocida -> {linea}")

        except Exception as e:
            print(f"[ERROR] Linea {num_linea}: Error al procesar -> {linea} ({e})")  # si hay un error, lo muestra y continua

def main():
    instrucciones = leer_instrucciones()
    ejecutar_instrucciones(instrucciones)
    turtle.done()

if __name__ == "__main__":
    main()