from datetime import datetime

import requests


def get_exchange_usdcop():

    URL = "https://open.er-api.com/v6/latest/USD"

    answer = requests.get(URL)
    information = answer.json()

    if information["result"] == "success":
        rate_cop = information["rates"]["COP"]

        return rate_cop
    else:
        print("Error in API information.")
        return None


def report_from_usd_cop(usd):
    data = get_exchange_usdcop()

    if data is None:
        print("It was not possible to get the information")
        return

    print("=== REAL-TIME CURRENCY CONVERTER ===")

    calculate = usd * data

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"At this time {time} the dollar-to-peso exchange rate is {data}")
    print(f"{usd} USD --> {calculate:,.2f} COP")


def report_from_cop_usd(cop):
    data = get_exchange_usdcop()

    if data is None:
        print("It was not possible to get the information")
        return

    print("=== REAL-TIME CURRENCY CONVERTER ===")

    calculate = cop / data

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"At this time {time} the dollar-topeso exchange rate is {data}")
    print(f"{cop} COP --> {calculate:,.2f} USD")
