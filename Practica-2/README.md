# practica-2
Mover una figura geométrica con el teclado usando la libreria turtle en Python

## Descripcion
Este proyecto es una práctica en **Python 3.10** utilizando la libreria **turtle**.  
El objetivo es aprender a mover una figura con el teclado.  
La figura se redibuja en cada movimiento para que se desplace sin dejar rastro.  

Extras añadidos (andaba aburrido y queria probar que podia hacer):
- Alternar entre cuadrado y circulo con "espacio".  
- Movimiento también con **WASD** (para que se mueva como un videojuego xd).  
- Uso de dos tortugas (`tCuadrado` y `tCirculo`) para mayor claridad.  
- Bucle de animación con `ontimer` a 16 ms (simula 60 FPS).

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
python practica2_movimientoG.py
```

4. Se abrira una ventana de turtle donde podras mover la figura con las flechas o con WASD.

---

## Estructura del proyecto

practica2_movimiento.py   # Codigo fuente principal
README.md                 # Documentacion del proyecto

---

## Funciones principales
- `dibujar()`  
  Redibuja la figura activa (cuadrado o circulo) en la posicion actual.  

- `step_loop()`  
  Bucle de animación que revisa las teclas presionadas y actualiza la posicion.  

- `toggle_figura()`  
  Alterna entre cuadrado y circulo al presionar "espacio".  

---

## Ejemplo de uso dentro del programa
- Mover la figura con las flechas ← ↑ → ↓.  
- Mover la figura con **WASD** (como en un videojuego).  
- Presionar **espacio** para alternar entre cuadrado y circulo.  

---

## Lo que se aprende con este proyecto
- Uso de eventos de teclado en turtle (`onkeypress`, `onkeyrelease`).  
- Manejo de animaciones con `ontimer`.  
- Redibujar figuras sin dejar rastros.  
- Organización del código usando múltiples tortugas (`tCuadrado`, `tCirculo`).  

---

## Posibles mejoras
- Agregar limites de ventana para que la figura no se salga de la ventana.  
- Permitir cambiar el color de la figura con otras teclas.  
- Agregar más figuras geométricas (triángulos, estrellas, etc.).

---

## Autor
Luis Sarabia - Proyecto desarrollado como práctica de programación en Python.
