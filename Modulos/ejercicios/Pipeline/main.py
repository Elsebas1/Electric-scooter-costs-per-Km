from procesador import ejecutar_pipeline

print("=== MENÚ DE OPCIONES ===")
print("1. instalar_db")
print("2. configurar_firewall")
print("3. respaldo_datos")
print("4. salir")

tarea = int(input("Digite un número de 1 a 4: "))

while tarea != 4:
    match tarea:
        case 1:
            ejecutar_pipeline("instalar_db")

        case 2:
            ejecutar_pipeline("configurar_firewall")

        case 3:
            ejecutar_pipeline("respaldo_datos")

        case _:
            print("Error. Dato incorrecto")

    tarea = int(input("Digite un número de 1 a 4: "))

print("\nSaliendo del sistema de automatización ! Hasta luego.")
