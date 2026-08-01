from datetime import datetime

import requests


def obtener_precios_mercado():
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    try:
        respuesta = requests.get(URL)
        datos = respuesta.json()
        return datos

    except Exception as e:
        print(f"Error to connect internet: {e}")
        return None


def generar_reporte():
    data = obtener_precios_mercado()

    if data is None:
        print("It was not possible to get the information")
        return

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bitcoin_price = data["bitcoin"]["usd"]
    ethereum_price = data["ethereum"]["usd"]

    compra_bitcoin = bitcoin_price / ethereum_price

    print(f"=== REPORT ===\n{time}")
    print(f"Bitcoin price: {int(bitcoin_price)}\nEthereum price: {int(ethereum_price)}")
    print(f"{compra_bitcoin:2f} Ethereums are needed to buy 1 bitcoin")


generar_reporte()
