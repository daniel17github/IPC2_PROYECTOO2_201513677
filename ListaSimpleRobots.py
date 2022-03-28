from Robot import Robot

class ListaSimpleRobots():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def CrearRobot(self,nombre,tipo,capacidad):

        nuevo = Robot(nombre,tipo,capacidad) #nuevo robot
        #print("Entro lo crea")
        self.size += 1
        
        if self.inicio is None:
            #print("Cabeza")
            self.inicio = nuevo
        else:
            #print("Siga entrando")
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarRobots(self):
        tmp = self.inicio
        while tmp is not None:
            #print("entra")
            print('Nombre:', tmp.nombre)
           # print('Nombre:', tmp.nombre, '\n Filas , Columnas : ',tmp.fila,',',tmp.columna, '\n  S, R : ',tmp.volterar,',',tmp.intercambiar)
           
            tmp = tmp.siguiente

    def getRobot(self, nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente
        return None

    
