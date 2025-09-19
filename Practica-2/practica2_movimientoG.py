"""
Practica 2
Mover una figura con el teclado
"""

import turtle

# Configuración de ventana (Encontre algunas cosas extra por ahí y se ve chido)
screen = turtle.Screen()
screen.title("Practica 2 - Mover una figura con el teclado")
screen.setup(width=800, height=600)
screen.tracer(0)  # Desactivar auto-dibujo para evitar parpadeos (muy importante para mi)

# Tortugas utilizadas
tCuadrado = turtle.Turtle(visible=False)  # Tortuga exclusiva para el cuadrado
tCirculo = turtle.Turtle(visible=False)   # Tortuga exclusiva para el circulo

for t in (tCuadrado, tCirculo):
    t.speed(0)
    t.penup()

# Pocisiones
pos_x, pos_y = 0, 0
lado = 100
figura = "cuadrado" # Figura inicial
pressed = set()
step_px = 10  # Velocidad ajustable (para que se mueva chido)

def dibujar():
    """Limpia y dibuja la figura activa en el centro (pos_x, pos_y)."""
    tCuadrado.clear()
    tCirculo.clear()

    if figura == "cuadrado":
        half = lado / 2
        tCuadrado.goto(pos_x - half, pos_y + half)
        tCuadrado.setheading(0)
        tCuadrado.pendown()
        for _ in range(4):
            tCuadrado.forward(lado)
            tCuadrado.right(90)
        tCuadrado.penup()
    else:
        radio = lado // 2
        lados = 100
        angulo = 360 / lados
        perimetro = 2 * 3.14159 * radio
        paso = perimetro / lados
        tCirculo.goto(pos_x, pos_y - radio)
        tCirculo.setheading(0)
        tCirculo.pendown()
        for _ in range(lados):
            tCirculo.forward(paso)
            tCirculo.left(angulo)
        tCirculo.penup()

    screen.update()


def step_loop():
    """Bucle de animacion para el movimiento continuo."""
    global pos_x, pos_y
    dx = (-step_px if "Left" in pressed or "a" in pressed else 0) + (step_px if "Right" in pressed or "d" in pressed else 0)
    dy = (step_px if "Up" in pressed or "w" in pressed else 0) + (-step_px if "Down" in pressed or "s" in pressed else 0)
    if dx or dy:
        pos_x += dx
        pos_y += dy
        dibujar()
    screen.ontimer(step_loop, 16)  # Cada 16 ms revisa la entrada (muy util al mantener presionada una tecla ya que simula 60 fps)

# Handlers
def on_press(key): pressed.add(key)
def on_release(key): pressed.discard(key)

def toggle_figura():
    """Alterna entre cuadrado y circulo."""
    global figura
    figura = "circulo" if figura == "cuadrado" else "cuadrado"
    dibujar()

def main():
    dibujar()
    screen.listen()

    # Flechas
    for key in ["Left", "Right", "Up", "Down"]:
        screen.onkeypress(lambda k=key: on_press(k), key)
        screen.onkeyrelease(lambda k=key: on_release(k), key)

    # WASD (para que se mueva como un videojuego xd)
    for key in ["w", "a", "s", "d"]:
        screen.onkeypress(lambda k=key: on_press(k), key)
        screen.onkeyrelease(lambda k=key: on_release(k), key)

    # Espacio para alternar la figura (no tenia nada mejor que hacer xd)
    screen.onkeypress(toggle_figura, "space")

    step_loop()
    turtle.done()

if __name__ == "__main__":
    main()
