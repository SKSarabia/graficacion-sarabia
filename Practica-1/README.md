# practica-1 
Utilizar la libreria turtle para dibujar figuras geometricas en Python

## Descripcion  
Este proyecto es una practica introductoria en **Python 3.10** utilizando la libreria **turtle**.  
El objetivo es aprender a dibujar figuras geometricas basicas (cuadrado, triangulo, circulo y linea recta) mediante funciones que reciben parametros como coordenadas y color.  
Cada figura esta implementada como una funcion independiente, lo que permite reutilizar el codigo y personalizar facilmente el tamano, posicion y color de las figuras.  

---

## Requisitos  
- Python **3.10** instalado en tu sistema.  
- No se requieren librerias externas, solo el modulo estandar `turtle`.  

---

## Como ejecutar el programa  
1. Descarga o clona este repositorio en tu computadora.  
2. Abre una terminal en la carpeta del proyecto.  
3. Ejecuta el archivo principal con:

```bash	
python practica1_figurasG_.py
```

4. Se abrira una ventana de turtle donde se dibujaran las figuras.

---

## Estructura del proyecto
practica1_figurasG_.py   # Codigo fuente principal
README.md       # Documentacion del proyecto

---

## Funciones principales
dibujar_cuadrado(x, y, lado, color) #Dibuja un cuadrado a partir de un punto inicial (x, y).

dibujar_triangulo(x, y, lado, color) #Dibuja un triangulo equilatero desde (x, y).

dibujar_circulo(x, y, radio, color) #Dibuja un circulo centrado en (x, y).

dibujar_linea(x1, y1, x2, y2, color) #Dibuja una linea recta entre dos puntos.

---

## Ejemplo de uso dentro del programa
# Dibujar un cuadrado verde en la esquina superior izquierda
dibujar_cuadrado(-200, 200, 100, "green")

# Dibujar un triangulo rojo en la esquina superior derecha
dibujar_triangulo(50, 200, 100, "red")

# Dibujar un circulo verde en el centro
dibujar_circulo(-50, -50, 60, "blue")

# Dibujar una linea negra en la parte inferior
dibujar_linea(-200, -200, 200, -200, "black")

---

## Lo que se aprende con este proyecto
- Uso basico de la libreria turtle.
- Manejo de coordenadas en un plano cartesiano.

---

## Posibles mejoras
- Agregar grosor de linea como parametro.
- Permitir relleno de figuras con begin_fill() y end_fill().

---

## Autor
Luis Sarabia - Proyecto desarrollado como practica de programacion en Python.
