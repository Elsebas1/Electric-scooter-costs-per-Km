# Módulo 1: Se encarga de la matemática del dinero y tiempo


def calcular_costo(horas):
    valor_por_hora = 5000

    if horas > 3:
        descuento = 0.1

        costo_descuento = valor_por_hora * horas * (1 - descuento)

        return int(costo_descuento)

    else:
        costo = valor_por_hora * horas

        return int(costo)
