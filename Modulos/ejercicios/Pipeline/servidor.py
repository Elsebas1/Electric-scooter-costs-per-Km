import json

# MODULO PARA ACCEDER A LOS DATOS


def get_task(task_name):
    RUTA_JSON = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Pipeline/tareas.json"
    try:
        with open(RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)

        if task_name in datos:
            return datos[task_name]

        else:
            return None

    except FileNotFoundError:
        print("That file does not exist.")


# ACTUALIZAR ESTADO


def complete_task(task_name):
    try:
        RUTA_JSON = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/Pipeline/tareas.json"

        with open(RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)

        if task_name in datos:
            datos[task_name]["estado"] = "pendiente"

        else:
            return False

        with open(RUTA_JSON, "w") as archivo_json:
            json.dump(datos, archivo_json, indent=4)

        return True

    except FileNotFoundError:
        return False
