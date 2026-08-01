# Archivo principal: Modela el flujo de simulación


from celdas import registrar_ingreso, registrar_salida, simular_paso_tiempo
from tarifas import calcular_costo

vehiculo = registrar_ingreso("FGH456")
simular_paso_tiempo()
simular_paso_tiempo()
simular_paso_tiempo()
simular_paso_tiempo()
horas_que_se_quedo = registrar_salida("FGH456")

total_a_pagar = calcular_costo(horas_que_se_quedo)

print(
    f"El vehícul {vehiculo} se quedó {horas_que_se_quedo} horas para un valor de {total_a_pagar}"
)
