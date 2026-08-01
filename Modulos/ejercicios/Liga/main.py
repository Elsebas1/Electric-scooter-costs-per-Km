# Módulo 3: Principal


from procesador import register_match, table

print("=== MENÚ DE OPCIONES ===")
print("1. Ver tabla de posiciones")
print("2. Registrar resultado de un partido")
print("3. salir")

tarea = int(input("Digite un número de 1 a 3: "))


while tarea != 3:
    match tarea:
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

    print("=== MENÚ DE OPCIONES ===")
    print("1. Ver tabla de posiciones")
    print("2. Registrar resultado de un partido")
    print("3. salir")

    tarea = int(input("Digite un número de 1 a 3: "))

print("\nSaliendo del sistema de automatización ! Hasta luego.")
