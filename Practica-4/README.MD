# practica-4  
Ejecutar instrucciones desde un archivo con la libreria turtle en Python  

## Descripcion  
Este proyecto es una práctica en **Python 3.10** utilizando la libreria **turtle**.  
El objetivo es leer un archivo externo (`dibujante.txt`) que contiene instrucciones de dibujo (cuadrado, triangulo, circulo, linea y teleport) y ejecutarlas en pantalla.  
Si una instruccion es invalida, el programa muestra un **ERROR** en la consola y continua con la siguiente.  

---  

## Requisitos  
- Python **3.10** instalado en tu sistema.  
- No se requieren librerias externas, solo el modulo estandar `turtle` (`os` solo soluciona un error de VSCode).  

---

## Como ejecutar el programa  
1. Descarga o clona este repositorio en tu computadora.  
2. Abre una terminal en la carpeta del proyecto.  
3. Asegurate de tener el archivo `dibujante.txt` con las instrucciones.  
4. Ejecuta el archivo principal con:  

```bash
python practica4_archivo_instruccionesG.py
```

5. Se abrira una ventana de turtle donde se dibujaran las figuras segun las instrucciones del archivo.

---

## Estructura del proyecto

practica4_archivo_instruccionesG.py   # Codigo fuente principal  
dibujante.txt                         # Archivo con instrucciones de dibujo  
README.md                             # Documentacion del proyecto  

---

## Funciones principales

- dibujar_cuadrado(x, y, lado, color)Dibuja un cuadrado en la posicion indicada.

- dibujar_triangulo(x, y, lado, color)Dibuja un triangulo equilatero en la posicion indicada.

- dibujar_circulo(x, y, radio, color)Dibuja un circulo aproximado.

- dibujar_linea(x1, y1, x2, y2, color)Dibuja una linea recta entre dos puntos.

- teleport(x, y)Mueve la tortuga a una coordenada sin dibujar.

- leer_instrucciones()Lee el archivo dibujante.txt y devuelve las instrucciones.

- ejecutar_instrucciones(instrucciones)Interpreta y ejecuta cada instruccion, mostrando un error si es invalida.

---

## Ejemplo de uso dentro del programa

Contenido de dibujante.txt:

CUADRADO -250 200 100 green
TRIANGULO -250 0 100 red
CIRCULO -200 -100 60 blue
LINEA -300 -250 -100 -250 black
INSTRUCCION DESCONOCIDA 0 0
TELEPORT 100 100
CUADRADO 100 100 50 purple

Salida:

- Se dibuja un cuadrado verde, un triangulo rojo, un circulo azul y una linea negra.

- La instruccion INSTRUCCION DESCONOCIDA genera un error en consola pero no detiene el programa.

- La tortuga se teletransporta a (100,100) y dibuja un cuadrado morado.

---

## Lo que se aprende con este proyecto

- Lectura y procesamiento de archivos de texto en Python.

- Interpretacion de instrucciones y ejecucion condicional.

- Manejo de errores con try/except.

---

## Posibles mejoras

- Agregar mas instrucciones.

- Implementar colores aleatorios si no se especifica uno.

---

## Autor
Luis Sarabia - Proyecto desarrollado como practica de programacion en Python.