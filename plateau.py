class Plateau:
    """
    Representa la meseta rectangular en Marte.
    """
    
    def __init__(self, anchura, altura):
        """Inicializa el plateau con las dimensiones dadas."""
        self.anchura = anchura
        self.altura = altura
    
    def es_posicion_valida(self, x, y):
        """Verifica si las coordenadas están dentro de los límites del plateau."""
        # Corregido: ahora compara x con self.anchura
        return 0 <= x <= self.anchura and 0 <= y <= self.altura