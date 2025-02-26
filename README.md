# Mars Rovers

## Descripción del Problema

Una escuadra de rovers robóticos será enviada por la NASA a una meseta en Marte. Esta meseta, que es curiosamente rectangular, debe ser navegada por los rovers para que sus cámaras a bordo puedan obtener una vista completa del terreno circundante y enviarla de vuelta a la Tierra.

La posición y ubicación de un rover se representa mediante una combinación de coordenadas x e y y una letra que representa uno de los cuatro puntos cardinales de la brújula. La meseta se divide en una cuadrícula para simplificar la navegación. Una posición de ejemplo podría ser 0, 0, N, lo que significa que el rover está en la esquina inferior izquierda y mirando hacia el Norte.

Para controlar un rover, la NASA envía una simple cadena de letras. Las posibles letras son 'L', 'R' y 'M'. 'L' y 'R' hacen que el rover gire 90 grados hacia la izquierda o derecha respectivamente, sin moverse de su posición actual. 'M' significa avanzar un punto de la cuadrícula y mantener la misma dirección.

Se asume que el cuadrado directamente al Norte de (x, y) es (x, y+1).

## Entrada y Salida

### Entrada:
- La primera línea de entrada son las coordenadas de la esquina superior derecha de la meseta, la esquina inferior izquierda se asume que es 0,0.
- La siguiente información se refiere a los rovers que han sido desplegados:
  - Cada rover tiene dos líneas de entrada. La primera línea proporciona la posición inicial del rover, y la segunda línea es una serie de instrucciones que le indican cómo explorar la meseta.
  - La posición está compuesta por dos enteros y una letra separados por espacios, correspondientes a las coordenadas x e y y la orientación del rover.

### Salida:
- La salida para cada rover debe ser sus coordenadas finales y orientación.

## Ejemplo

### Entrada de prueba:
```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Salida esperada:
```
1 3 N
5 1 E
```

## Implementación

Este proyecto está implementado en Python y sigue un enfoque orientado a objetos. Se ha dividido en diferentes módulos para mejorar la legibilidad, mantenibilidad y extensibilidad del código.

### Estructura del Proyecto

```
mars_rovers/
├── orientacion.py  # Maneja las direcciones y rotaciones
├── plateau.py      # Define la meseta y sus límites
├── rover.py        # Implementa la lógica del rover
└── main.py         # Punto de entrada del programa
```

### Clases y Módulos

#### Orientacion (orientacion.py)
Esta clase maneja todo lo relacionado con las direcciones cardinales, rotaciones y movimientos. Implementa:
- Constantes para las direcciones (N, E, S, W)
- Mapeo de direcciones a movimientos (dx, dy)
- Métodos para girar a la izquierda y derecha
- Método para obtener el desplazamiento según la dirección

#### Plateau (plateau.py)
Representa la superficie rectangular donde se mueven los rovers:
- Almacena las dimensiones de la meseta
- Verifica si una posición está dentro de los límites válidos

#### Rover (rover.py)
Implementa la lógica del rover:
- Mantiene la posición y dirección actual
- Ejecuta instrucciones (L, R, M)
- Verifica si un movimiento es válido antes de realizarlo

#### Main (main.py)
Contiene la lógica principal del programa:
- Parsea la entrada
- Crea y configura los objetos necesarios
- Ejecuta las instrucciones para cada rover
- Genera la salida esperada

## Cómo ejecutar

1. Clona este repositorio:
```bash
git clone https://github.com/yourusername/mars-rovers.git
cd mars-rovers
```

2. Ejecuta el programa con Python:
```bash
python main.py
```

Por defecto, el programa utiliza los datos de prueba especificados en el problema. Si deseas usar datos diferentes, puedes modificar la variable `entrada_prueba` en la función `main()` o descomentar las líneas para leer desde la entrada estándar.

## Enfoque de Diseño

El diseño de esta solución se basa en los siguientes principios:

1. **Separación de responsabilidades**: Cada clase tiene una función específica y bien definida.
2. **Encapsulación**: Los detalles de implementación están ocultos dentro de las clases correspondientes.
3. **Extensibilidad**: El diseño permite agregar fácilmente nuevas funcionalidades, como nuevos tipos de instrucciones o comportamientos.
4. **Legibilidad**: El código está estructurado de manera clara y con nombres descriptivos.

## Mejoras potenciales

Algunas mejoras que podrían implementarse en el futuro:

1. Añadir validación de entrada más robusta
2. Implementar manejo de excepciones para casos extremos
3. Agregar detección de colisiones entre rovers
4. Crear una interfaz gráfica para visualizar el movimiento de los rovers
5. Permitir cargar instrucciones desde archivos externos

## ME DISCULPO SI EL CODIGO ESTA MEDIO FEO, PERO ESTOY UN POCO OXIDADO CON LAS PRUEBAS TECNICAS Y DE ALGORITMIA,
## PD: ESTUVO INTERESANTE EL PROBLEMA
