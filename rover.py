from orientacion import Orientacion


class Rover:
    
    def __init__(self, x, y, direccion, plateau):
        self.x = x 
        self.y = y 
        self.direccion = direccion 
        self.plateau = plateau 

    
    def ejecutar_instrucciones(self, instrucciones):

        for instruccion in instrucciones:
            if instruccion == 'L':
                self.girar_izquierda()
            elif instruccion == 'R':
                self.girar_derecha()
            elif instruccion == 'M':
                self.mover() 
    
    def girar_izquierda(self):
        self.direccion = Orientacion.girar_izquierda(self.direccion) 

    def girar_derecha(self):
        self.direccion = Orientacion.girar_derecha(self.direccion)
    
    def mover(self):
        
        dx, dy = Orientacion.obtener_movimiento(self.direccion)

        nueva_x = self.x + dx 
        nueva_y = self.y + dy

        if self.plateau.es_posicion_valida(nueva_x, nueva_y):
            self.x = nueva_x
            self.y = nueva_y 

    def obtener_posicion(self):
        return f"{self.x} {self.y} {self.direccion}"