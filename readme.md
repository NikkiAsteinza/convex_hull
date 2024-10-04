# Convex Hull Visualizer en Pygame

## Descripción

Este proyecto es un visualizador de Convex Hull implementado en Pygame. Permite a los usuarios seleccionar hasta 50 puntos en la pantalla y calcular el Convex Hull de esos puntos. El resultado se visualiza en tiempo real, mostrando el polígono Convex Hull que encierra todos los puntos seleccionados. También se proporciona una opción para reiniciar la selección y comenzar de nuevo.

## Enfoque

El enfoque utilizado en este script se basa en el algoritmo de **Graham Scan** para calcular el Convex Hull, que es un polígono que puede encerrar todos los puntos dados en un conjunto. A continuación se describen las secciones clave y la lógica detrás de cada una:

1. **Inicialización de Pygame y configuración de colores:**
   - Se inicializa Pygame y se definen los colores utilizados en la visualización.
   - Se establece el tamaño de la ventana y otros parámetros de configuración.

2. **Funciones de dibujo:**
   - Se definen funciones para dibujar puntos, líneas y botones en la pantalla, utilizando la biblioteca Pygame.
   - `drawPoint`: Dibuja un punto en la pantalla.
   - `drawLine`: Dibuja una línea entre dos puntos.
   - `drawButton`: Dibuja un botón en la pantalla y renderiza el texto correspondiente.

3. **Lógica de selección de puntos:**
   - El usuario puede hacer clic en la pantalla para seleccionar puntos hasta un máximo de 50.
   - Si se hace clic en el botón "Convex Hull", se calcula el Convex Hull de los puntos seleccionados, siempre y cuando haya al menos 3 puntos.

4. **Cálculo del Convex Hull:**
   - La función `convexHull` calcula el Convex Hull utilizando el enfoque de barrido (sweep).
   - Se ordenan los puntos por coordenadas y se construyen las partes inferior y superior del polígono Convex Hull.
   - Se utiliza la función `cross` para determinar la orientación de los puntos y garantizar que se mantenga la convexidad.

5. **Visualización del resultado:**
   - Una vez calculado el Convex Hull, se visualiza dibujando líneas entre los puntos del hull.
   - Los puntos seleccionados se dibujan en blanco, mientras que el Convex Hull se dibuja en azul.

6. **Reinicio de la selección:**
   - Después de calcular el Convex Hull, las instrucciones y el botón "Convex Hull" desaparecen, y aparece un botón "Reset".
   - Al hacer clic en "Reset", se borran todos los puntos seleccionados y el Convex Hull, permitiendo al usuario comenzar de nuevo.

## Requisitos

- Python 3.x
- Pygame

## Instrucciones para ejecutar

1. Asegúrate de tener Python y Pygame instalados en tu sistema.
2. Descarga o clona este repositorio.
3. Ejecuta el script utilizando el siguiente comando:
```
python main.py
```
4. Haz clic en la ventana para seleccionar puntos.
5. Haz clic en el botón "Convex Hull" para calcular el Convex Hull.
6. Para reiniciar, haz clic en el botón "Reset".

## Contribuciones

Las contribuciones son bienvenidas. Si tienes mejoras o sugerencias, siéntete libre de abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
