# MÓDULO 2: PROCESAMIENTO
# Paso 1: Importar servidor con sus funciones.
from servidor import cargar_inventario, guardar_inventario


def procesar_venta(nombre_producto, cantidad):

    # Paso 2: Llamar el diccionario.
    carga = cargar_inventario()

    # Paso 3: Verificar que exista el nombre del producto en el diccionario.
    if nombre_producto in carga:
        producto = carga[nombre_producto]

        # Paso 4: Verificar la cantidad de stock solicitada con la que hay en el inventario.

        if producto["stock"] >= cantidad:
            producto["stock"] = producto["stock"] - cantidad

            # Paso 5: Actualizar el diccionario

            guardar_inventario(carga)

            total_venta = producto["precio_usd"] * cantidad
            print("¡Operación exitosa!")
            print(f"Producto: {producto['nombre']}")
            print(f"Cantidad vendida {cantidad}")
            print(f"El total de la venta fue: {total_venta} USD")

        else:
            print(
                f"No hay stock suficiente para el producto {carga[nombre_producto]['nombre']}"
            )

    else:
        print(f"Error el producto {nombre_producto} no existe en el inventario.")
