menup = ["Ver listado de pinturas", "Buscar pintura", "Agregar pintura" , "Eliminar pintura" , "Exportar pintura"]
from pathlib import Path
import json
import os
import csv

home = Path(__file__).parent
rutaj = Path(home/"pinturas.json")
def crear_archivo(ruta):
    if not ruta.exists():
        ruta.touch()
        print("El archivo no existia pero ha sido creado correctamente")
    else:
        pass


def listar(lista):
    for ind, opt in enumerate(lista):
        print(f"{ind + 1}. {opt}")



def ver_pinturas(rutaj):
    with open(rutaj,"r") as archivo:
        jsonfile = json.load(archivo)
        for lista in jsonfile:
            print(lista)

        

def agregar_pintura(ruta):
    with open(ruta, mode='a+') as stream:
        nombre = input("Cual es el color de la pintura?")
        while True:
            tipo = input("1.   Acrilico   2.   Latex\nIngresa una opcion valida")
            if tipo == "1":
                tipo = "Acrilico"
                break
            elif tipo == "2":
                tipo = "Latex"
                break
            else:
                print("Error: no seleccionaste una opcion valida")
        valor = int(input("Ingrese el valor de la pintura"))
        stock = int(input("Ingrese su respectivo stock"))
        codigo = 380560 + 1
        nueva_pintura = {

                
            "codigo" : codigo,
            "nombre" : nombre,
            "tipo" : tipo,
            "valor" : valor,
            "stock" : stock
        }
        nueva_lista = []
        nueva_lista.append(nueva_pintura)
        json.dump(nueva_lista, stream,indent=4)
        os.system("cls")
        print("Pintura agregada correctamente")


def buscar_pintura(ruta):
    with open(ruta,"a+"):
        codigo = input("Ingrese el codigo de la pintura que desea buscar\n")
        if codigo in ruta:
            print(codigo[codigo])
        else:
            print("El codigo que ingresaste no se encuentra en nuestro inventario")


def eliminar_pintura(ruta):
    with open(ruta,"a+") as stream:
        codigo = input("Ingresa el codigo de la pintura que deseas eliminar")
        if codigo in stream:
            del(codigo)
            os.system("cls")
            print("Pintura eliminada correctamente")
        else:
            os.system("cls")
            print("Pintura no encontrada, por lo tanto no eliminaste nada")

        

