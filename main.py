from plateau import Plateau
from rover import Rover

def procesar_entrada(entrada):
    """
    Procesa la entrada y devuelve la salida esperada.
    """
    # Dividimos la entrada en líneas
    lineas = entrada.strip().split('\n')
    
    # Primera línea: dimensiones del plateau
    dimensiones = lineas[0].split()
    max_x = int(dimensiones[0])
    max_y = int(dimensiones[1])
    
    # Creamos el plateau con las dimensiones dadas
    plateau = Plateau(max_x, max_y)
    
    # Procesar la información de cada rover
    resultados = []
    i = 1
    # Corregido: ahora usa i < len(lineas) en lugar de 1 < len(lineas)
    while i < len(lineas):
        # Posición inicial del rover
        pos_inicial = lineas[i].split()
        x = int(pos_inicial[0])
        y = int(pos_inicial[1])
        direccion = pos_inicial[2]
        
        # Instrucciones para el rover
        instrucciones = lineas[i + 1]
        
        # Crear y mover el rover
        rover = Rover(x, y, direccion, plateau)
        rover.ejecutar_instrucciones(instrucciones)
        
        # Añadir la posición final a los resultados
        resultados.append(rover.obtener_posicion())
        
        # Avanzar al siguiente rover
        i += 2
    
    # Unimos los resultados con saltos de línea
    return '\n'.join(resultados)


def main():
    """Función principal del programa."""
    # Para pruebas, usamos la entrada de ejemplo
    entrada_prueba = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
    
    resultado = procesar_entrada(entrada_prueba)
    print(resultado)
    
    # Para una aplicación real, podríamos leer de la entrada estándar:
    # import sys
    # entrada_usuario = sys.stdin.read()
    # resultado = procesar_entrada(entrada_usuario)
    # print(resultado)


if __name__ == "__main__":
    main()