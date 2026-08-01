# Módulo 2

from servidor import save_accounts, upload_accounts


def check_account(number):

    check = upload_accounts()

    if check is None:
        print("System Error when attempting to connect to the bank.")

    if number not in check:
        print("Error: The account login does not exist.")

    print(f"El titular de la cuenta es: {check[number]['titular']}")
    print(f"Posee un saldo de: {check[number]['saldo_usd']}")
    print(f"El tipo de cuenta que maneja es: {check[number]['tipo_cuenta']}")


def withdraw_money(number_account, amount):
    upload = upload_accounts()

    # print(upload[number_account]["saldo_usd"])

    if upload is None:
        print("System Error when attempting to connect to the bank.")
        return False

    if number_account not in upload:
        print("Error: The account login does not exist")

        return False

    target = upload[number_account]

    if amount > 500:
        print("Alert: the withdrwal amount per transaction is 500 USD")

        return False

    elif amount > target["saldo_usd"]:
        print(f"Error: Insufficient funds. Available funds {target['saldo_usd']} USD.")

        return False

    else:
        target["saldo_usd"] = target["saldo_usd"] - amount

        save_accounts(upload)

        print(
            f"¡Retiro exitoso! Ha retirado {amount} USD. Nuevo saldo {target['saldo_usd']}"
        )
        return True
