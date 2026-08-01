# Módulo 2: Controla el inventario de puestos / vehículos

vehiculos_activos = {
    "ABC123": 2,
    "XYZ789": 5,
}


def registrar_ingreso(placa):

    vehiculos_activos[placa] = 0

    return placa


def simular_paso_tiempo():

    for placa, horas in vehiculos_activos.items():
        vehiculos_activos[placa] = horas + 1


def registrar_salida(placa):

    # 1. Busca las horas usando la placa como clave.
    horas_acumuladas = vehiculos_activos[placa]

    # 2. Borrar el vehículo del diccionario
    del vehiculos_activos[placa]

    # 3. Devolver las horas
    return horas_acumuladas
