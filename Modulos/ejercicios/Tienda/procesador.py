# MÓDULO 2: PROCESAMIENTO

from servidor import upload_inventory, save_inventory


def process_sell(product_name, amount):

    upload = upload_inventory()


    if product_name in upload:
        product = upload[product_name]


        if product["stock"] >= amount:
            product["stock"] = product["stock"] - amount



            save_inventory(upload)

            total_sell = product["precio_usd"] * amount
            print("¡Operation success!")
            print(f"product: {product['nombre']}")
            print(f"amount selt {amount}")
            print(f"The total sale was: {total_sell} USD")

        else:
            print(
                f"There are not enough stock to the product {upload[product_name]['nombre']}"
            )

    else:
        print(f"Error the product {product_name} does not exist in the inventory.")
