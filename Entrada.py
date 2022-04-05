from cgi import print_arguments
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
    print("2.MISIONES ")
    print("3.DATOS GUARDADOS")
    print("4.Datos Personales")
    print("5.Mostrar Datos actuales")
    print("6.Salir")
    print("---------------------------------------")
    


def CargarArchivo(ruta):
    #print("Ruta que entra para cargar los archivos:  " + ruta)
    #C:\Users\Dany\Documents\USAC\IPC2 2022\Laboratorio\Proyecto2\ArchivoPrueba.xml
    #C:\Users\Dany\Documents\USAC\IPC2 2022\Laboratorio\Proyecto2\prueba1.xml
    tree= ET.parse(ruta)
    raiz= tree.getroot()
    global validass
    
    # FOR QUE ME MUESTRA QUE DATOS TENGO 
    for elemento in raiz:
        #print(elemento.tag)
        validasss = elemento.tag

        #GUARDO LOS ROBOTS EN MI LISTA
        if  validasss == "robots":
            #print('entro en robot')
            for subelementorobot in elemento.iter('robot'):
                nombreR=""
                capacidad=""
                RtipoR =""
                #print(subelementorobot.tag)
                #print(subelementorobot.find('nombre').text)
                nombreR= subelementorobot.find('nombre').text
                #print(subelementorobot.find('nombre').attrib['tipo'])
                tipoR=str(subelementorobot.find('nombre').attrib['tipo'])
                #print(subelementorobot.find('nombre').attrib['capacidad'])
                capacidadR= str(subelementorobot.find('nombre').attrib['capacidad'])
                #CREO LOS ROBOTS QUE VIENEN EN EL ARCHIVO DE ENTRADA            
                ListaRobots.CrearRobot(nombreR,tipoR,capacidadR)
                print("LOS ROBOTS FUERON GUARADADOS EXITOSAMENTE")
        #GUARDO LAS CIUDADES EN MI LISTA
        else:
            #print('entro en ciudades')
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
                    #LA LISTA ME TIENE QUE VENIR SIN ESPACIOS ANTES DE LAS COMILLAS Y FINAL DE LAS COMILLAS
                    #print(lista)
                    numerofila= str(subsubelemento.attrib['numero'])

                    contador = 1
                    #FOR DONDE METO LOS DATOS A LA MATRIZ 
                    for dato in lista:
                        #GUARDO DATOS EN LA MATRIZ (X , Y , CARACTER)
                        #print(numerofila,contador,dato)
                        Posicion.matriz.insertar(numerofila,contador,dato)
                        #print(dato)   
                        contador+=1
                        #print(contador)
                    #print("imprime->"+str(contador))
            #print(subelemento.find('ciudad').text)
            print("CIUDADES GUARDADOS CON EXITO")
    print("DATOS GUARDADOS CORRECTAMENTE")
             
        

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
        print("************     MISIONES     ************")
        print("1. MISION DE RESCATE")
        print("2. MISION DE EXTRACCION DE RECURSOS")
        elec1 = input("SELECCIONE UNA OPCION")

        if elec1 == "1":
            #VERIFICANDO SI HAY CHAPIN RESCUE EN MIS DATOS
            #SI NO HAY CHAPIN RESCUE NO HAGO LAS MISIONES

            #IDENTIFICAR LA CIUDAD QUE QUIERO UTILIZAR


            #VERIFIAR SI HAY UNIDADES CIVILES EN LA CIUDAD PARA PODER REALIZARLO
            print("")


        elif elec1 == "2" :
            print("")
            #VERIFIANDO SI HAY CHAPIN FIGHTER 
            #SI NO HAY CHAPIN FIGHTER NO HAGO LAS MISIONES

            

        else:
            print("OPCION INCORRECTA SELECCIONE UN NUMERO ENTRE 1 Y 2")



    elif Eleccion == "3":
        print("DATOS QUE HAY GUARDADOS POR EL MOMENTO ...")
        print("ROBOTS -----------------------------")
        ListaRobots.mostrarRobots()
        
        print(" ")
        print("CIUDADES-------------------------------")
        ListaCiudades.mostrarCiudad()

        datox = input("INGRESE EL NOMBRE DE LA CIUDAD PARA GENERAR GRAFICA: ")
        
        ciudax = ListaCiudades.getCiudad(datox)

        if ciudax is None :
            print("CIUDAD NO EXISTE INGRESE BIEN EL NOMBRE ")
        else:
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

