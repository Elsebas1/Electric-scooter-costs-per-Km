from servidor import completar_tarea, obtener_tarea

RAM_MAXIMA_GB = 5


def ejecutar_pipeline(nombre_tarea):

    tarea_encontrada = obtener_tarea(nombre_tarea)

    if tarea_encontrada is None:
        print("Error. La tarea no existe en el sistema.")
        return False

    if tarea_encontrada["requisito_ram_gb"] <= RAM_MAXIMA_GB:
        completar_tarea(nombre_tarea)
        print(
            f"¡Éxito! Tarea {nombre_tarea} ejecutada y estado actualizado a completado."
        )
        return True
    else:
        print(
            f"Alerta: No hay suficientes recursos para {nombre_tarea}. Requiere {tarea_encontrada['requisito_ram_gb']}GB y el límite es {RAM_MAXIMA_GB}GB."
        )

        return False
