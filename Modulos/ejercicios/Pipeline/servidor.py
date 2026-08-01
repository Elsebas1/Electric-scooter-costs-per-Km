import json

# MODULO PARA ACCEDER A LOS DATOS


def obtener_tarea(nombre_tarea):
    RUTA_JSON = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Pipeline/tareas.json"
    try:
        with open(RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)

        if nombre_tarea in datos:
            return datos[nombre_tarea]

        else:
            return None

    except FileNotFoundError:
        print("Este archivo no existe")


# ACTUALIZAR ESTADO


def completar_tarea(nombre_tarea):
    try:
        RUTA_JSON = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Pipeline/tareas.json"

        with open(RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)

        if nombre_tarea in datos:
            datos[nombre_tarea]["estado"] = "pendiente"

        else:
            return False

        with open(RUTA_JSON, "w") as archivo_json:
            json.dump(datos, archivo_json, indent=4)

        return True

    except FileNotFoundError:
        return False
