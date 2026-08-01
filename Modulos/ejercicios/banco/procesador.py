# Módulo 2

from servidor import save_accounts, upload_accounts


def check_account(number):

    check = upload_accounts()

    if check is None:
        print("System Error when attempting to connect to the bank.")

    if number not in check:
        print("Error: The account login does not exist.")

    print(f"The account holder is: {check[number]['titular']}")
    print(f"It has a balance of {check[number]['saldo_usd']}")
    print(f"The type of bank account you have is {check[number]['tipo_cuenta']}")


def withdraw_money(number_account, amount):
    upload = upload_accounts()

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
            f"¡Succesful withdrawal! you have withdrawal {amount} USD. New balance {target['saldo_usd']}"
        )
        return True
