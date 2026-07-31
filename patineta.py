"""
Electric scooter cost
"""

print("--- Electric scooter cost validation ---")


def kilometres_information():

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

    print("\n---Menu---")
    print("1. log mileage")
    print("2. View the cost of each recorded kilometer.")
    print("3. View the cost of total distances")
    print("4. Leave")

    option = int(input("Enter an option from 1 to 4 "))

    while option < 1 or option > 3:
        print("Type a number from 1 to 4")

    while option >= 1 and option <= 3:
        match option:
            case 1:
                distance_list, mant_cost, km_mant = kilometres_information()

                print(f"The recorded values are: {distance_list}")
            case 2:
                check = cost(distance_list, mant_cost, km_mant)

                print(f"{check}")

            case 3:
                total_path = total_distance(distance_list, mant_cost, km_mant)

                print(f"{total_path}")

            case 4:
                print("Leaving...")
                break

            case _:
                print("Error. Tpye a number from 1 to 3.")

        print("\n---Menu---")
        print("1. log mileage")
        print("2. View the cost of each recorded kilometer.")
        print("3. View the cost of total distances")
        print("4. Leave")

        option = int(input("Enter an option from 1 to 4 "))


main()
