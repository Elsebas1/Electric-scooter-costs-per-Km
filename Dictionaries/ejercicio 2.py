purchasing = [
    {"product": "Laptop Asus", "price": 3_000_000, "category": "technology"},
    {"product": "Café Juan Valdez", "price": 40_000, "category": "food"},
    {"product": "Audífonos Sony", "price": 500_000, "category": "technology"},
]

# Tabla de descuentos (Porcentaje que se debe restar al price)
dictionary_discounts = {"technology": 0.10, "food": 0.05}


def apply_discounts(products_list, offer):

    for article in products_list:
        discounts = offer.get(article["category"], 0.0)

        new_price = article["price"] * (1 - discounts)

        article["price"] = int(new_price)

    return products_list


new_list = apply_discounts(purchasing, dictionary_discounts)
print("--- RESUMEN ---")

for new in new_list:
    print(f"{new['product']} ---> {new['price']}")
