class Robot: #Clase Nodo
    def __init__(self, nombre,tipo,capacidad):
       # self.posIniciox = posIniciox
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.siguiente = None
   
    def gerNombre(self):
        return self.nombre