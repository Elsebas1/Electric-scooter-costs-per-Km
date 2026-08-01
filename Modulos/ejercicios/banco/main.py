# Módulo 3: Principal

from procesador import check_account, withdraw_money

print("=== OPTIONS MENU ===")
print("1. Check balance")
print("2. Withrawal money")
print("3. Leave")

option = int(input("Enter a number from 1 to 3"))


while option != 3:
    match option:
        case 1:
            number = input("Enter your account number: ")

            check_account(number)

        case 2:
            account = input("Enter your account number ")
            withdraw = int(input("Enter the amount of money you wish to withdrawal: "))
            withdraw_money(account, withdraw)

        case _:
            print("Error. Wrong information")

    print("=== OPTIONS MENU ===")
    print("1. Check balance")
    print("2. Withrawal money")
    print("3. Leave")

    option = int(input("Enter a number from 1 to 3: "))

print("\nLeaving the automation system.")
