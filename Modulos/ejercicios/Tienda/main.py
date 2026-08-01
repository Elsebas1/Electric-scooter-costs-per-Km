# Módulo 3: PRINCIPAL

from procesador import procesar_venta

print("=== MENÚ DE OPCIONES ===")
print("1. nintendo_switch")
print("2. playstation_5")
print("3. xbox_series_x")
print("4. salir")

tarea = int(input("Digite un número de 1 a 4: "))


while tarea != 4:
    match tarea:
        case 1:
            stock = int(
                input("Digite los productos que necesita de la bodega para vender: ")
            )
            procesar_venta("nintendo_switch", stock)

        case 2:
            stock = int(
                input("Digite los productos que necesita de la bodega para vender: ")
            )
            procesar_venta("playstation_5", stock)

        case 3:
            stock = int(
                input("Digite los productos que necesita de la bodega para vender: ")
            )
            procesar_venta("xbox_series_x", stock)

        case _:
            print("Error. Dato incorrecto")

    print("=== MENÚ DE OPCIONES ===")
    print("1. nintendo_switch")
    print("2. playstation_5")
    print("3. xbox_series_x")
    print("4. salir")

    tarea = int(input("Digite un número de 1 a 4: "))

print("\nSaliendo del sistema de automatización ! Hasta luego.")
