from servidor_liga import read_file, write_file


# TABLA DE POSICIONES
def table():
    positions = read_file()

    ordenados = sorted(
        positions.items(), key=lambda item: item[1]["puntos"], reverse=True
    )

    for equipo, value in ordenados:
        print(equipo, value["puntos"])


# REGISTROS DE RESULTADOS
def register_match(local, scores_local, visitante, scores_visit):

    file = read_file()

    if file is None:
        print("System Error when attempting to connect to the league.")
        return False

    if local not in file or visitante not in file:
        print("Error: The name of the team/s is wrong.")
        return False

    # PARTIDOS JUGADOS
    file[local]["partidos_jugados"] += 1
    file[visitante]["partidos_jugados"] += 1

    # GOLES

    file[local]["goles_a_favor"] += scores_local
    file[local]["goles_en_contra"] += scores_visit

    file[visitante]["goles_a_favor"] += scores_visit
    file[visitante]["goles_en_contra"] += scores_local

    if scores_local > scores_visit:
        print(f" {local}: {scores_local} | {visitante}: {scores_visit}")

        # PUNTOS
        file[local]["puntos"] += 3

    elif scores_local < scores_visit:
        print(f"{visitante}: {scores_visit} | {local}: {scores_local}")

        # PUNTOS
        file[visitante]["puntos"] += 3

    else:
        print(f"{local} {scores_local} | {visitante}: {scores_visit}")

        # PUNTOS
        file[local]["puntos"] += 1
        file[visitante]["puntos"] += 1

    write_file(file)

    print("=== MATCHES PLAYED ===")
    print(
        f"{local}: {file[local]['partidos_jugados']} | {visitante}: {file[visitante]['partidos_jugados']}"
    )

    print("=== GOALS SCORED===")

    print(
        f"{local}: {file[local]['goles_a_favor']} | {visitante}: {file[visitante]['goles_a_favor']}"
    )
