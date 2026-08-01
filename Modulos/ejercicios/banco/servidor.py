# Módulo 1
import json


def upload_accounts():
    try:
        RUTA = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/banco/banco.json"

        with open(RUTA, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("This file does not exist.")

        return None


def save_accounts(data):

    RUTA = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/banco/banco.json"

    with open(RUTA, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return True
