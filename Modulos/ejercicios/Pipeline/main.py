from procesador import executed_pipeline

print("=== OPTION MENU===")
print("1. Download_db")
print("2. firewall_configuration")
print("3. backup_data")
print("4. leave")

option = int(input("Enter a number from 1 to 4: "))

while option != 4:
    match option:
        case 1:
            executed_pipeline("instalar_db")

        case 2:
            executed_pipeline("configurar_firewall")

        case 3:
            executed_pipeline("respaldo_datos")

        case _:
            print("Error. Wrong information")

    option = int(input("Enter a number from 1 to 4: "))

print("\nLeaving automate system.")
