# neon-platformer  
Juego sencillo en Python usando la libreria **pygame**  

## Descripcion  
Este proyecto es un pequeño juego tipo *platformer* desarrollado en **Python 3.10** con la libreria **pygame**.  
El objetivo es controlar un jugador que puede moverse a izquierda y derecha, saltar sobre plataformas y evitar enemigos.  

El profesor proporcionó el código base y la tarea consistía en **corregir las colisiones**.  
En mi caso, ajusté las **paredes laterales** para que el jugador no pudiera salirse de la pantalla.  

---  

## Requisitos  
- Python **3.10** instalado en tu sistema.  
- Libreria **pygame** instalada:  

## Como ejecutar el programa
1. Descarga o clona este repositorio en tu computadora.
2. Abre una terminal en la carpeta del proyecto.
3. Instala Pygame con:

```bash
python -m pip install pygame
```

4. Ejecuta el archivo principal con:

```bash
python neon_platformer.py
```

5. Se abrira una ventana de 900x500 pixeles con el juego.

---

## Controles
- Flecha izquierda (←): mover al jugador a la izquierda.
- Flecha derecha (→): mover al jugador a la derecha.
- Espacio: saltar (solo si esta en el suelo).

---

## Estructura del proyecto
neon_platformer.py   # Codigo fuente principal
README.md            # Documentacion del proyecto

---

## Funciones principales
- dibujar_neon(rect, color, ancho=2)Dibuja un rectangulo con efecto neon alrededor de jugadores, plataformas y enemigos.

## Bucle principal del juego:
- Maneja eventos de teclado.
- Aplica gravedad y movimiento.
- Detecta colisiones con plataformas y enemigos.
- Dibuja en pantalla todos los elementos.
- Incrementa los puntos con el tiempo.
- Ejemplo de uso dentro del juego
- El jugador inicia en la parte inferior izquierda.
- Puede saltar sobre plataformas para esquivar enemigos.
- Si toca un enemigo, el juego termina.
- Los puntos aumentan automaticamente con el tiempo.

---

## Lo que se aprende con este proyecto
- Uso de la libreria pygame para crear juegos 2D.
- Manejo de eventos de teclado.
- Implementacion de gravedad y colisiones.
- Dibujo de figuras con efectos visuales (neon).
- Estructura basica de un bucle de juego.

---

## Posibles mejoras
- Agregar musica y efectos de sonido.
- Implementar mas niveles o plataformas dinamicas.
- Incluir un sistema de vidas o reinicio al perder.

---

## Autor
Luis Sarabia - Proyecto desarrollado como practica de programacion en Python con pygame.