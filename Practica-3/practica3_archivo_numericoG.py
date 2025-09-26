"""
Practica 3
Archivo Numerico
"""

import turtle
import os

# Configuracion de ventana
screen = turtle.Screen()
screen.title("Practica 3 - Archivo Numerico")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(0) # velocidad maxima a la tortuga
t.penup()
t.hideturtle()

# Asignacion de colores
colores = {
    "0": "black",
    "1": "red",
    "2": "green",
    "3": "blue",
    "4": "yellow",
    "5": "purple",
    "6": "orange",
    "7": "cyan",
    "8": "pink",
    "9": "brown"
}

# Funciones base
def leer_matriz():
    """
    Lee el archivo matriz.txt y devuelve la matriz.
    """
    base = os.path.dirname(__file__)
    filename = os.path.join(base, "matriz.txt")   # ruta real al archivo matriz (lo encontre en un foro para la solucion a un error en VSCode)

    matriz = []
    for line in open(filename, encoding="utf-8"):
        seq = line.split()
        fila = [w for w in seq]
        matriz.append(fila)
    return matriz

# Pintado de los pixeles
def pintar_pixel(x, y, size, color):
    """
    Dibuja un cuadrado relleno simulando un pixel.
    """
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.penup()

#Dibuja la matriz
def dibujar_matriz(matriz, pixel=5):
    """
    Dibuja la matriz en pantalla, cada numero corresponde a un color.
    """
    inicio_x = - (len(matriz[0]) * pixel) // 2
    inicio_y = (len(matriz) * pixel) // 2

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            color = colores.get(valor, "white")  # default es blanco (por si acaso xd)
            x = inicio_x + j * pixel
            y = inicio_y - i * pixel
            pintar_pixel(x, y, pixel, color)
    screen.update()

def main():
    matriz = leer_matriz()
    screen.tracer(300)   # muestra la actualizacion de pixeles (se puede eliminar junto a screen.update para el dibujo instantaneo)
    dibujar_matriz(matriz, pixel=5)
    screen.update()
    turtle.done()

if __name__ == "__main__":
    main()