"""
Electric scooter cost
"""

print("--- Electric scooter cost validation ---")


def informacion_kilometros():

    record = input("¿Do you wish to record km? (Y / N): ").lower()
    maintenance_cost = 250_000
    maintance_km = 800

    route = []
    while record == "y":
        try:
            path = float(input("How many kilometres will you cover today?: "))

            if path <= 0:
                print("That information can not be recorded.")
                continue

            else:
                route.append(path)
        except ValueError:
            print("It is just possible written numbers.")

        record = input("¿Do you wish to record km? (Y / N): ").lower()

    return route, maintenance_cost, maintance_km


def cost(kilometres, maintance_cost, km_mant):

    maintance_per_km = maintance_cost / km_mant
    print(f"The km cost is: {maintance_per_km}")

    results = []
    for km in kilometres:
        km_cost = maintance_per_km * km
        results.append(f"El costo de {km} km es: {km_cost:.0f}")

    set_limpio = set(results)

    return set_limpio


def total_distance(total_kilometres, mant_cost, km_mant):

    addition = sum(total_kilometres)

    if addition > 0:
        distance = (mant_cost * addition) / km_mant

    return (
        f"A total of {addition} km was covered at a total cost of: {distance:.0f} pesos"
    )


def main():

    print("\n---Menú---")
    print("1. Registrar kilometros")
    print("2. Ver costo de cada kilometro registrado")
    print("3. Ver costo de los recorridos totales")
    print("4. Salir")

    opcion = int(input("Digite una opción entre 1 y 4: "))

    while opcion < 1 or opcion > 3:
        print("Digite un número entre 1 y 4")

    while opcion >= 1 and opcion <= 3:
        match opcion:
            case 1:
                lista_recorridos, mant_cost, km_mant = informacion_kilometros()

                print(f"Los valores registados son: {lista_recorridos}")
            case 2:
                revision = cost(lista_recorridos, mant_cost, km_mant)

                print(f"{revision}")

            case 3:
                totalidad_recorridos = total_distance(
                    lista_recorridos, mant_cost, km_mant
                )

                print(f"{totalidad_recorridos}")

            case 4:
                print("Saliendo...")
                break

            case _:
                print("Error. Digite un dato entre 1 y 3")

        print("\n---Menú---")
        print("1. Registrar kilometros")
        print("2. Ver costo de cada kilometro registrado")
        print("3. Ver costo de los recorridos totales")
        print("4. Salir")

        opcion = int(input("Digite una opción entre 1 y 4: "))


main()
