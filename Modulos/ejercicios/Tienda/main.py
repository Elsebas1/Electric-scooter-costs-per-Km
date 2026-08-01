# Módulo 3: PRINCIPAL

from procesador import process_sell

print("=== OPTION MENU ===")
print("1. nintendo_switch")
print("2. playstation_5")
print("3. xbox_series_x")
print("4. leave")

option = int(input("Enter a number from 1 to 4 "))


while option != 4:
    match option:
        case 1:
            stock = int(
                input("Enter the products you need in the store to sell: ")
            )
            process_sell("nintendo_switch", stock)

        case 2:
            stock = int(
                input("Enter the products you need in the store to sell ")
            )
            process_sell("playstation_5", stock)

        case 3:
            stock = int(
                input("Enter the products you need in the store to sell ")
            )
            process_sell("xbox_series_x", stock)

        case _:
            print("Error. Dato incorrecto")

    print("=== OPTION MENU===")
    print("1. nintendo_switch")
    print("2. playstation_5")
    print("3. xbox_series_x")
    print("4. Leave")

    option = int(input("Enter a number from 1 to 4 "))

print("\nLeaving the automate system.")
