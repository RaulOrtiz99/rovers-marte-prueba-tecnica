class Orientacion:
    """
    Clase para manejar las orientaciones cardinales y sus rotaciones.
    """
    
    # Definimos las orientaciones como una lista, para facilitar las rotaciones
    DIRECCIONES = ['N', 'E', 'S', 'W']
    
    # Definimos los cambios de posición para cada dirección (dx, dy)
    MOVIMIENTOS = {
        'N': (0, 1),    # Norte: sin cambio en x, +1 en y
        'E': (1, 0),    # Este: +1 en x, sin cambio en y
        'S': (0, -1),   # Sur: sin cambio en x, -1 en y (corregido)
        'W': (-1, 0)    # Oeste: -1 en x, sin cambio en y (añadido)
    }
    
    @classmethod
    def girar_izquierda(cls, direccion_actual):
        """Gira 90 grados a la izquierda desde la dirección actual."""
        indice_actual = cls.DIRECCIONES.index(direccion_actual)
        return cls.DIRECCIONES[(indice_actual - 1) % 4]
    
    @classmethod
    def girar_derecha(cls, direccion_actual):
        """Gira 90 grados a la derecha desde la dirección actual."""
        indice_actual = cls.DIRECCIONES.index(direccion_actual)
        return cls.DIRECCIONES[(indice_actual + 1) % 4]
    
    @classmethod
    def obtener_movimiento(cls, direccion):
        """Devuelve el movimiento (dx, dy) para una dirección dada."""
        return cls.MOVIMIENTOS[direccion]