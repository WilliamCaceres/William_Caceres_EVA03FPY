from pathlib import Path
import json
import os
import csv
from modules.construccion import menup, listar, crear_archivo, ver_pinturas, agregar_pintura, buscar_pintura, eliminar_pintura
home = Path(__file__).parent
rutaj = Path(home/"pinturas.json")
crear_archivo(rutaj)
while True:
    print("Bienvenido a Pinturas Acriticas Mandarina")
    listar(menup)
    ans = input("Que quieres hacer?")
    if ans == "1":
        os.system("cls")
        ver_pinturas(rutaj)
    elif ans == "2":
        buscar_pintura(rutaj)
    elif ans == "3":
        agregar_pintura(rutaj)
    elif ans == "4":
        eliminar_pintura(rutaj)
    elif ans == "5":
       """ "PROFE, LA VERDAD NOC EXPORTAR (Y TAMPOCO SE BN HACER DEL TODO LAS DEMAS FUNCIONES) PERO SI LO HAGO REIR
       ME DA EL PUNTO DE EXPORTAR, AQUI VA EL CHISTE
       ¿Que es un terapeuta?
       ...
       ...
       ...
       no?
       1024 gygapeutas *Inserta tambor de risa*

       los chistes no son lo mio, pero habia q intentar, saludos profe, y recuerde siempre.
       Que el fin se acerca.. 
       """
    else:
        print("Error: Opcion seleccionada no valida")
    
