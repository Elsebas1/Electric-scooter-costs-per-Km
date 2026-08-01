# Módulo 1

import json


def read_file():

    try:
        RUTA = "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/liga/liga.json"

        with open(RUTA, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("This file does not exist.")


def write_file(data):

    RUTA = (
        "/Users/sebastiangomez/Python /Modulos/archivos json/ejercicios/liga/liga.json"
    )

    with open(RUTA, "w") as file_writting:
        json.dump(data, file_writting, indent=4)

    return True
