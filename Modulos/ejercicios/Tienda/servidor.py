# MÓDULO 1:: LECTURA Y ESCRITURA DEL ARCHIVO JSON
import json


def cargar_inventario():
    try:
        RUTA_ARCHIVO = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Tienda/bodega.json"

        with open(RUTA_ARCHIVO, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print("No se encontró el archivo")
        return None


def guardar_inventario(datos):

    RUTA_ARCHIVO = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Tienda/bodega.json"

    with open(RUTA_ARCHIVO, "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4)
