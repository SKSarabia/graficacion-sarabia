# pylint: disable=E1101 # Deshabilita el error de pylint para atributos de turtle (no encontre otra manera)

"""
practica-1
Utilizar la libreria turtle para dibujar figuras geometricas en Python
"""

import turtle as t   # se importa turtle y se le da el nombre 't'


def dibujar_cuadrado(x, y, lado, color):
    """
    Dibuja un cuadrado en la posicion (x, y).

    Parametros:
        x (int/float): coordenada X inicial.
        y (int/float): coordenada Y inicial.
        lado (int/float): longitud de cada lado del cuadrado.
        color (str): color de las lineas del cuadrado.
    """
    t.penup()
    t.goto(x, y)   # mueve la tortuga a la posicion inicial
    t.pendown()
    t.color(color)
    for _ in range(4):   # cuadrado de cuatro lados lol
        t.forward(lado)
        t.right(90)


def dibujar_triangulo(x, y, lado, color):
    """
    Dibuja un triangulo equilatero en la posicion (x, y).

    Parametros:
        x (int/float): coordenada X inicial.
        y (int/float): coordenada Y inicial.
        lado (int/float): longitud de cada lado del triangulo.
        color (str): color de la linea del triangulo.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(3):   # tres lados iguales (equilatero)
        t.forward(lado)
        t.left(120)


def dibujar_circulo(x, y, radio, color):
    """
    Dibuja un circulo con "escalones".

    Parametros:
        x (int/float): coordenada X del centro.
        y (int/float): coordenada Y del centro.
        radio (int/float): radio del circulo.
        color (str): color de la linea del circulo.
    """
    t.penup()
    t.goto(x, y - radio)   # se baja la tortuga para centrar el circulo
    t.pendown()
    t.color(color)
    for _ in range(360):   # 360 pasos de 1 grado (hacer escalones)
        t.forward(2 * 3.1416 * radio / 360)
        t.left(1)


def dibujar_linea(x1, y1, x2, y2, color):
    """
    Dibuja una linea recta entre dos puntos.

    Parametros:
        x1 (int/float): coordenada X inicial.
        y1 (int/float): coordenada Y inicial.
        x2 (int/float): coordenada X final.
        y2 (int/float): coordenada Y final.
        color (str): color de la linea.
    """
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.goto(x2, y2)


def main():
    """
    Funcion principal que ejecuta los ejemplos de dibujo:
    - Un cuadrado verde.
    - Un triangulo rojo.
    - Un circulo azul.
    - Una linea negra.
    """
    t.speed(5)   # velocidad 5 para que no sea tan tortuga (no aplica con el circulo XD)

    dibujar_cuadrado(-250, 200, 100, "green")
    dibujar_triangulo(-250, 0, 100, "red")
    dibujar_circulo(-200, -100, 60, "blue")
    dibujar_linea(-300, -250, -100, -250, "black")

    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()
