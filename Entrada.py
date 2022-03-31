import xml.etree.ElementTree as ET
import re

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
    


'''matriz = MatrizDispersa()

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


matriz.graficarNeato('MatrizDispersa')

matriz.recorridoPorFila(50)
matriz.recorridoPorColumna(2)

NodoEncontrado = matriz.ubicarCoordenada(50,20)'''

print('Hola mundo')

def CargarArchivo(ruta):
    print("Ruta que entra para cargar los archivos:" + ruta)
    #C:\Users\Dany\Documents\USAC\IPC2 2022\Laboratorio\Proyecto2\ArchivoPrueba.xml
    #C:\Users\Dany\Documents\USAC\IPC2 2022\Laboratorio\Proyecto2\prueba1.xml
    tree= ET.parse(ruta)
    raiz= tree.getroot()
    global validass
    
    # FOR QUE ME MUESTRA QUE DATOS TENGO 
    for elemento in raiz:
        print(elemento.tag)
        validasss = elemento.tag

        #GUARDO LOS ROBOTS EN MI LISTA
        if  validasss == "robots":
            print('entro en robot')
            for subelementorobot in elemento.iter('robot'):
                nombreR=""
                capacidad=""
                RtipoR =""
                #print(subelementorobot.tag)
                print(subelementorobot.find('nombre').text)
                nombreR= subelementorobot.find('nombre').text
                print(subelementorobot.find('nombre').attrib['tipo'])
                tipoR=str(subelementorobot.find('nombre').attrib['tipo'])
                print(subelementorobot.find('nombre').attrib['capacidad'])
                capacidadR= str(subelementorobot.find('nombre').attrib['capacidad'])
                #CREO LOS ROBOTS QUE VIENEN EN EL ARCHIVO DE ENTRADA            
                ListaRobots.CrearRobot(nombreR,tipoR,capacidadR)

        #GUARDO LAS CIUDADES EN MI LISTA
        else:
            print('entro en ciudades')
            for subelemento in elemento.iter('ciudad'):
                nombreC=""
                filaC=""
                columnaC=""

                #print(subelemento.find('nombre').text)
                nombreC= subelemento.find('nombre').text
                #print(subelemento.find('nombre').attrib['filas'])
                filaC=str(subelemento.find('nombre').attrib['filas'])
                #print(subelemento.find('nombre').attrib['columnas'])
                columnaC= str(subelemento.find('nombre').attrib['columnas'])
                #CREO LOS ROBOTS QUE VIENEN EN EL ARCHIVO DE ENTRADA            
                ListaCiudades.CrearCiudad(nombreC,filaC,columnaC)
                #print(subelemento.tag)

            #GUARDANDO LOS DATOS EN LA MATRIZ
                for subsubelemento in subelemento.iter('fila'):
                    #BUSCANDO LA RUTA A LA QUE SE LE VA A AGREGAR LA MATRIZ
                    #print(subelemento.find('nombre').text)
                    Posicion =  ListaCiudades.getCiudad(subelemento.find('nombre').text)
                    #print(Posicion)
                    #print(subsubelemento.text)
                    lista =re.findall("[ECR*\s]" , subsubelemento.text)
                    print(lista)
                    numerofila= str(subsubelemento.attrib['numero'])

                    contador = 1
                    #FOR DONDE METO LOS DATOS A LA MATRIZ 
                    for dato in lista:
                        #GUARDO DATOS EN LA MATRIZ (X , Y , CARACTER)
                        print(numerofila,contador,dato)
                        Posicion.matriz.insertar(numerofila,contador,dato)
                        print(dato)   
                        contador+=1
                        #print(contador)
                    print("imprime->"+str(contador))
            #print(subelemento.find('ciudad').text)

        
      
        

    print("-----------------------")  

    #FOR QUE ME GUARDA LOS DATOS DEL ARCHIVO DE ENTRADA
    #print("ETIQUETAS QUE ESTOY AGARRANDO ")
        #EMPEZANDO A GUARDAR DATOS DEL ARCHIVO DE ENTRADA

       
        


while True:
    menu()
    Eleccion= input("Ingrese la opcion que desea realizar: ")
    
    if Eleccion =="1":
        print("Bienvenido Opcion Cargar Archivo ...!")
        ruta = input("Ingrese la Ruta de su archivo ")
        CargarArchivo(ruta)

    elif Eleccion == "2":
        print("Desplegando matrices...")







    elif Eleccion == "3":
        print("ROBOTS QUE TENGO...")
        ListaRobots.mostrarRobots()
        
        print("--------------")
        print("CIUDADES QUE TENGO")
        ListaCiudades.mostrarCiudad()

        datox = input("INGRESE EL NOMBRE DE LA CIUDAD PARA GENERAR GRAFICA")
        ciudax = ListaCiudades.getCiudad(datox)
        ciudax.matriz.graficarNeato(datox)        

        
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

