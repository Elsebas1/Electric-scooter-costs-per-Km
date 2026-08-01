# Módulo 3: Principal


from procesador import register_match, table

print("=== OPTION MENU ===")
print("1. View standings")
print("2. Record a match result")
print("3. Leave")

option = int(input("Enter a number from 1 to 3: "))


while option != 3:
    match option:
        case 1:
            table()

        case 2:
            local = input("Write the name of the home team: ")
            visit = input("Write the name of the visit team: ")
            score_local = int(input("Write how many goals the home team scores: "))
            score_visit = int(input("Write how many goals the visit team scores:"))

            register_match(local, score_local, visit, score_visit)

        case _:
            print("Error. Dato incorrecto")


    print("=== OPTION MENU ===")
    print("1. View standings")
    print("2. Record a match result")
    print("3. Leave")
    option = int(input("Enter a number from 1 to 3: "))

print("\nLeaving of automation system")
