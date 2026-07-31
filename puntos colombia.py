print("-" * 60)
print("Analysis of Colombian Points with American Express Cards")
print("-" * 60)


def credit_cards():

    cards = [
        ["American Express Blue", 1183],
        ["American Express Green", 883],
        ["American Express Gold", 750],
        ["American Express Platinum", 633],
    ]

    return cards


def check_cards(cards):

    for card in cards:
        print(f"{card[0]} -> {card[1]} ")


def choice(cards_list):

    user = input("Which American Express credit card do you have?: ").lower()

    for card in cards_list:
        card_type = card[0]
        points = card[1]
        if user == card_type.lower():
            print(f"\nThe American Express Card is: {card}")

            print(
                f"\nFor every {points} you spend with this card, you will receive 1 point."
            )

            return user, points
    print("\nThat card does not exist in te American Express World")
    return None, None


def user_expenses(user_choice, user_points):

    if user_choice is None or user_points is None:
        return "\nMistake. You must select a credit card first (Option 2)."

    else:
        try:
            user_dos = float(input("How much money are you going to spend: "))

            calculation = user_dos / user_points

            return f"Your colombian points is: {calculation}"
        except ValueError:
            print("Write numbers, no words")


def main():
    list_of_Cards = credit_cards()
    user_card = None
    points = None

    print("--- Principal Menu ---")
    print("1. Check the credit cards list")
    print("2. Choice the credit card you have")
    print(
        "3. Calculate the colombian points amount you would receive if you spend money"
    )
    print("4. Salir")

    option = int(input("Choose an option between 1 and 4: "))

    while option < 1 or option > 4:
        print("Mistake. You have to choose an option between 1 and 4")

    while option >= 1 and option <= 4:
        match option:
            case 1:
                check_cards(list_of_Cards)

            case 2:
                user_card, points = choice(list_of_Cards)

            case 3:
                expenses = user_expenses(user_card, points)

                print(expenses)

            case 4:
                print("Leaving...")
                break

            case _:
                print("Mistake. Choose an option between 1 and 4")

        print("--- Principal Menu ---")
        print("1. Check the credit cards list")
        print("2. Choice the credit card you have")
        print(
            "3. Calculate the colombian points amount you would receive if you spend money"
        )
        print("4. Salir")

        option = int(input("Choose an option between 1 and 4: "))


main()
