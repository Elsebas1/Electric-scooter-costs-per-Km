# MÓDULO 1:: LECTURA Y ESCRITURA DEL ARCHIVO JSON
import json


def upload_inventory():
    try:
        FILE_ROUTE = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Tienda/bodega.json"

        with open(FILE_ROUTE, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print("The file was not found.")
        return None


def save_inventory(datos):

    FILE_ROUTE = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Tienda/bodega.json"

    with open(FILE_ROUTE, "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4)
