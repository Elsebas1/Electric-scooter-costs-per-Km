from divisas import report_from_cop_usd, report_from_usd_cop

print("=== REAL-TIME CURRENCY CONVERTER ===")
print("1. From USD to COP")
print("2. From COP to USD")
print("3. Leave")

option = int(input("Write the option do you want to choose: "))

while option != 3:
    match option:
        case 1:
            usd = float(input("How many dollars do you wish to exchage for pesos?: "))

            report_from_usd_cop(usd)

        case 2:
            cop = float(input("How many COPS do you wish to exchange for dollars?: "))

            report_from_cop_usd(cop)

        case _:
            print("\nInvalid option. Please choose a number between 1 and 2.\n")

    print("=== REAL-TIME CURRENCY CONVERTER ===")
    print("1. From USD to COP")
    print("2. From COP to USD")
    print("3. Leave")

    option = int(input("Write the option do you want to choose: "))

print("\nThank you for using our program.")
