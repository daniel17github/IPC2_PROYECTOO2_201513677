import xml.etree.ElementTree as ET

from MatrizDispersa import MatrizDispersa
from ListaSimpleRobots import ListaSimpleRobots
from ListaSimpleCiudades import ListaSimpleCiudades
ListaRobots = ListaSimpleRobots() # CREANDO LISTA VACIA PARA LOS ROBOTS
ListaCiudades = ListaSimpleCiudades() # CREANDO LISTA VACIA PARA LA CIUDAD
print("EMPEZANDO EL PROYECTO    ")
print("Iniciando el menu para  ")


def menu():

    print("\n        PISOS ARTESANALES S.A          ")
    print("\n---------------------------------------")
   
    print("             MENU")
    print("1.Cargar archivo")
    print("2.Elegir patron ")
    print("3.Mostrar Datos Ordenados")
    print("4.Datos Personales")
    print("5.Mostrar Datos actuales")
    print("6.Salir")
    print("---------------------------------------")
    


matriz = MatrizDispersa()

matriz.insertar(1, 1, 'Andre')     
matriz.insertar(1, 2, 'Jose Jorge')
matriz.insertar(1, 3, 'Nathan')
matriz.insertar(1, 4, 'Kemel')
matriz.insertar(2, 1, '*')
matriz.insertar(2, 2, '*')
matriz.insertar(2, 3, '*')
matriz.insertar(2, 4, '*')
matriz.insertar(3, 1, '*')
matriz.insertar(3, 2, 'hola')
matriz.insertar(3, 3, '*')
matriz.insertar(3, 4, '*')
matriz.insertar(4, 1, '*')
matriz.insertar(4, 2, '*')
matriz.insertar(4, 3, '*')
matriz.insertar(4, 4, '*')
matriz.insertar(8, 9, '*')
matriz.insertar(9, 8, '*')
matriz.insertar(2, 2, '*')
matriz.insertar(15,20,'*')
matriz.insertar(15,2, 'Luis Enrique')
matriz.insertar(15,4,'*')

#matriz.graficarNeato('Matriz Dispersa')

matriz.recorridoPorFila(50)
matriz.recorridoPorColumna(2)

NodoEncontrado = matriz.ubicarCoordenada(50,20)

print('Hola mundo')

def CargarArchivo(ruta):
    print("Ruta que entra para cargar los archivos:" + ruta)
    #C:\Users\Dany\Documents\USAC\IPC2 2022\Laboratorio\Proyecto2\ArchivoPrueba.xml
    tree= ET.parse(ruta)
    raiz= tree.getroot()

    for elemento in  raiz:
        print("ENTRANDO AL ARCHIVO DE ENTRADA")




while True:
    menu()
    Eleccion= input("Ingrese la opcion que desea realizar: ")
    
    if Eleccion =="1":
        print("Bienvenido Opcion Cargar Archivo ...!")
        ruta = input("Ingrese la Ruta de su archivo ")
        CargarArchivo(ruta)

    elif Eleccion == "2":
        print("Desplegando Busquedas...")
                 


    elif Eleccion == "3":
        print("PISOS ORDENADOS ALFABETICAMENTE...")
       
        
        
    elif Eleccion == "4":
        print("---------------------------------------------------")
        print("Introduccion a la Programacion y Computacion 2...")
        print("Ingenieria en Ciencias y Sistemas")
        print("Cuarto Semestre")
        print("Daniel Alejandro Orozco Melgar")
        print("201513677")
        print("---------------------------------------------------")
    

    elif Eleccion == "5":
        print("DATOS...")
        
       
    elif Eleccion == "6":
             
        print("Saliendo...")
        print("Saliendo..")
        print("Saliendo.")
        break
                           
    else:
        print("Opcion Incorrecta elige una entre el rango del 1-6")

