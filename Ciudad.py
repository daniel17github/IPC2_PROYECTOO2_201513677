from MatrizDispersa import MatrizDispersa

class Ciudad: #Clase Nodo
    def __init__(self, nombre,fila,columna):
       # self.posIniciox = posIniciox
        self.nombre = nombre
        self.fila = fila    
        self.columna = columna
        self.matriz = MatrizDispersa()
        self.siguiente = None
   
    def gerNombre(self):
        return self.nombre

    def getMatriz(self):
        return self.matriz