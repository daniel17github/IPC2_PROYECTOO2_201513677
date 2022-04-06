from Ciudad import Ciudad

class ListaSimpleCiudades():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def CrearCiudad(self,nombre,fila,columna):

        nuevo = Ciudad(nombre,fila,columna) #nueva Ciudad
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

    def mostrarCiudad(self):
        tmp = self.inicio
        while tmp is not None:
            #print("entra")
            print('Nombre:', tmp.nombre)
           # print('Nombre:', tmp.nombre, '\n Filas , Columnas : ',tmp.fila,',',tmp.columna, '\n  S, R : ',tmp.volterar,',',tmp.intercambiar)
           
            tmp = tmp.siguiente

    def getCiudad(self, nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente
        return None

    def mostrarCiudadRecurso(self,militar):
        jeje = "3"
        tmp= self.inicio
        
        while tmp is not None:
            if tmp.militar == militar:
                print(tmp.nombre)
                jeje="4"
                #return tmp.nombre
            tmp = tmp.siguiente
        return jeje

    def mostrarCiudadCivil(self,civil):
        jeje = "5"
        tmp= self.inicio
        
        while tmp is not None:
            if tmp.civil == civil:
                print(tmp.nombre)
                jeje="6"
                #return tmp.nombre
            tmp = tmp.siguiente
        return jeje

    