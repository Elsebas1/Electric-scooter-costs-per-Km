"""
Un usuario desea saber el costo total por dos meses de ir al gimnasio. El costo total incluye el costo de la mensualidad y el costo de ir en su scooter.
"""

valor_mantenimiento = 250_000
kilometros_mantenimiento = 800
meses = 2
dias = 31
total = dias * meses
numero_domingos = 9
kilometros_por_dia = 8

dias_reales = total - numero_domingos

print(dias_reales)

valor_por_kilometro = valor_mantenimiento / kilometros_mantenimiento


valor = kilometros_por_dia * valor_por_kilometro * dias_reales

print(f"\nEl valor de ir por dos meses al gimnasio en scooter es: {valor}")


print("--- GIMNASIO ----")
costo = 38_250

valor_total_dos_meses = (costo * 4) + valor

print(f"\nEl valor total en los dos meses es de: {valor_total_dos_meses}")

valor_anual = costo * 12

valor_promocion_total = valor_anual + valor_total_dos_meses

print(f"En total el costo de ir al spining es: {valor_promocion_total} ")
