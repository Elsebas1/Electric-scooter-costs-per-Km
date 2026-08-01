# Módulo 3: Principal

from procesador import check_account, withdraw_money

print("=== MENÚ DE OPCIONES ===")
print("1. Ver saldo")
print("2. Retirar dinero")
print("3. salir")

tarea = int(input("Digite un número de 1 a 3: "))


while tarea != 3:
    match tarea:
        case 1:
            number = input("Escriba su número de cuenta: ")

            check_account(number)

        case 2:
            account = input("Escriba su número de cuenta: ")
            withdraw = int(input("Digite la cantidad de dinero que piensa retirar: "))
            withdraw_money(account, withdraw)

        case _:
            print("Error. Dato incorrecto")

    print("=== MENÚ DE OPCIONES ===")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. salir")

    tarea = int(input("Digite un número de 1 a 3: "))

print("\nSaliendo del sistema de automatización ! Hasta luego.")
