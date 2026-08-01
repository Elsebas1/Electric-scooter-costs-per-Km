customer = {
    "name": "andres_dev",
    "membership": "gold",
    "accumulated_points": 150,
    "purchases": [
        {"product": "mechanical keyboard", "price": 300_000, "category": "technology"},
        {"product": "Mouse Pad XL", "price": 80_000, "category": "technology"},
        {"product": "Café Gourmet", "price": 45000, "category": "food"},
    ],
}

points_rules = {"blue": 1000, "green": 800, "gold": 500, "platinum": 200}


def calculate_purchases(products_list):

    total_purchases = 0

    for article in products_list:
        total_purchases += article["price"]

    return total_purchases


def process_purchase(customer_profile, points):

    bill = calculate_purchases(customer_profile["purchases"])

    point_value = points.get(customer_profile["membership"], 1000)

    print(
        f"Customer {customer['name']} holds a {customer['membership'].upper()} membership and will earn 1 point for every {point_value} COP spent"
    )

    new_points = bill // point_value

    print(f"The new points earned from the purchase are {new_points}")

    customer_profile["accumulated_points"] += new_points

    customer_profile["purchases"].clear()

    return bill, customer_profile


total_expenditure, updated_client = process_purchase(customer, points_rules)

print("\n--- FINAL SUMMARY OF THE OPERATION ---")
print(
    f"The customer {updated_client['name'].capitalize()} spent a total of {total_expenditure} COP"
)
print(f"Your new total point balance is: {updated_client['accumulated_points']}.")
print(f"Purchase status: {updated_client['purchases']}.")
