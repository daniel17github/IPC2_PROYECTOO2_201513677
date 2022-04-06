from MatrizDispersa import MatrizDispersa

class Ciudad: #Clase Nodo
    def __init__(self, nombre,fila,columna):
       # self.posIniciox = posIniciox
        self.nombre = nombre
        self.fila = fila    
        self.columna = columna
        self.civil = "no"
        self.militar = "no"
        self.matriz = MatrizDispersa()
        self.siguiente = None
   
    def getNombre(self):
        return self.nombre

    def getMatriz(self):
        return self.matriz

    def getCivil(self):
        return self.civil

    def setCivil(self,civil):
        self.civil = civil

    def getMilitar(self):
        return self.militar

    def setMilitar(self,militar):
        self.militar = militar