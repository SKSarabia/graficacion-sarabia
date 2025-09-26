# practica-3  
Dibujar una matriz de colores con la librería turtle en Python  

## Descripcion  
Este proyecto es una práctica en **Python 3.10** utilizando la librería **turtle**.  
El objetivo es leer un archivo externo (`matriz.txt`) que contiene una **matriz de 100x100** con números del **0 al 9**, asignar un color a cada número y dibujar un “pixel art” en pantalla.  
Cada número representa un color distinto y la tortuga se mueve a la coordenada correspondiente para pintar el pixel.  

Extras añadidos:  
- Uso de `os.path` para asegurar que el archivo `matriz.txt` se lea correctamente sin importar desde dónde se ejecute el programa.  

---  

## Requisitos  
- Python **3.10** instalado en tu sistema.  
- No se requieren librerías externas, solo el módulo estándar `turtle` (`os` solo soluciona un error de VSCode).  

---  

## Como ejecutar el programa  
1. Descarga o clona este repositorio en tu computadora.  
2. Abre una terminal en la carpeta del proyecto.  
3. Ejecuta el archivo principal con:

```bash
python practica3_archivo_numericoG.py
```

4. Se abrirá una ventana de turtle donde se dibujará la matriz de colores.

---

## Estructura del proyecto
practica3_archivo_numericoG.py   # Código fuente principal  
matriz.txt                       # Archivo con la matriz 100x100  
README.md                        # Documentación del proyecto  

---

## Funciones principales
- leer_matriz()Lee el archivo matriz.txt y devuelve la matriz como lista de listas.
- pintar_pixel(x, y, size, color)Dibuja un cuadrado relleno simulando un pixel en la coordenada indicada.
- dibujar_matriz(matriz, pixel=5)Recorre la matriz y dibuja cada número con el color asignado.

---

## Ejemplo de uso dentro del programa
- El archivo matriz.txt contiene números del 0 al 9.
- Cada número corresponde a un color (ejemplo: 0 = negro, 1 = rojo, 2 = verde, etc.).
- Al ejecutar el programa, se dibuja un mosaico de 100x100 píxeles de colores.

---

## Lo que se aprende con este proyecto
- Lectura de archivos externos en Python.
- Manejo de listas y matrices.
- Representación gráfica de datos con turtle.
- Relación entre datos numéricos y visualización en pantalla.

---

## Posibles mejoras
- Permitir más colores agregando números adicionales en la matriz.
- Ajustar dinámicamente el tamaño de la ventana según el tamaño de la matriz.

---

## Fuentes de información
- Python Software Foundation. (2023). turtle — Gráficos con Turtle. Documentación oficial de Python 3.9.23. Recuperado de https://docs.python.org/es/3.9/library/turtle.html
- Stack Overflow en español. (2019). Obtener la ruta del directorio en Python pero en una carpeta antes. Recuperado de https://es.stackoverflow.com/questions/518231/obtener-la-ruta-del-directorio-en-python-pero-en-una-carpeta-antes

---

## Autor
Luis Sarabia - Proyecto desarrollado como práctica de programación en Python.