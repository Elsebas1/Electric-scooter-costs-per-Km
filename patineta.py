"""
Electric scooter cost
"""

print("--- Electric scooter cost validation ---")


def informacion_kilometros():

    record = input("¿Desea registrar kilometraje? (S / N): ").lower()
    valor_mantenimiento = 250_000
    kilometros_mantenimiento = 800

    recorrido = []
    while record == "s":
        try:
            camino = float(input("¿Cuántos kilometros va a recorrer hoy?: "))

            if camino <= 0:
                print("Este dato no se puede registrar")
                continue

            else:
                recorrido.append(camino)
        except ValueError:
            print("Solo es posible colocar números")

        record = input("¿Desea registrar kilometraje? (S / N): ").lower()

    return recorrido, valor_mantenimiento, kilometros_mantenimiento


def costos(kilometros, valor_mant, km_mant):

    mantenimiento_por_kilometro = valor_mant / km_mant
    print(f"El costo por kilometro es igual a: {mantenimiento_por_kilometro}")

    results = []
    for km in kilometros:
        costo_kilometro = mantenimiento_por_kilometro * km
        results.append(f"El costo de {km} km es: {costo_kilometro:.0f}")

    set_limpio = set(results)

    return set_limpio


def recorrido_total(kilometros_totales, valor_mant, km_mant):

    suma = sum(kilometros_totales)

    if suma > 0:
        total_recorrido = (valor_mant * suma) / km_mant

    return f"En total se recorrieron {suma} km con un costo total de: {total_recorrido:.0f} pesos"


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
                lista_recorridos, valor_mant, km_mant = informacion_kilometros()

                print(f"Los valores registados son: {lista_recorridos}")
            case 2:
                revision = costos(lista_recorridos, valor_mant, km_mant)

                print(f"{revision}")

            case 3:
                totalidad_recorridos = recorrido_total(
                    lista_recorridos, valor_mant, km_mant
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
