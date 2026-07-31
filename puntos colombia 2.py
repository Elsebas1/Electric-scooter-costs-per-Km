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
        print(f"Type of card: {card[0]} | value of each point: {card[1]} COP")


def number_cards(cards_list):
    try:
        user = int(input("Out of the 4 credit cards, how many do you have?: "))

        if user <= 0 or user > 4:
            print(
                "\n That is not possible. To the program run correctly, you must have between 1 or 4 type of cards."
            )
            return None

        else:
            user_cards = []
            i = 0
            while i < user:
                names = input("Can you write the cards names do you have?: ").lower()

                tarjeta_valida = False

                for card in cards_list:
                    card_type = card[0]
                    points = card[1]

                    if names == card_type.lower():
                        print(
                            f"Very well, you have a {names} card. I am adding it in the system."
                        )
                        user_cards.append([card_type, points])
                        tarjeta_valida = True

                        i += 1
                if not tarjeta_valida:
                    print("\nThat card does not exist in te American Express World")

            return user_cards

    except ValueError:
        print("You must enter an integer number")


def calculate_points(new_list):

    try:
        user_spend = float(input("How much money do you think spend?: "))

        if user_spend < 0:
            print("The ammount cannot be negative.")
            return None

        else:
            for card in new_list:
                card_name = card[0]
                points = card[1]

                calculate = user_spend / points

                print(f" - {card_name}: You receive {int(calculate)} points.")

    except ValueError:
        print("Enter a valid number.")


def main():
    new_list = None
    credits = credit_cards()

    print("--- Principal Menu ---")
    print("1. Check the credit cards list")
    print("2. Write the credit card you have")
    print(
        "3. Calculate the colombian points amount you would receive if you spend money"
    )
    print("4. Salir")

    option = int(input("Choose an option betwwen 1 and 4: "))

    while option < 1 or option > 4:
        print("Mistake. You have to choose an option between 1 and 4")

    while option != 4:
        match option:
            case 1:
                check_cards(credits)

            case 2:
                new_list = number_cards(credits)

                print(new_list)

            case 3:
                if new_list is None:
                    print("You need to register your cards first.")

                else:
                    calculate_points(new_list)

            case 4:
                print("Leaving...")
                break

            case _:
                print("You have to choose an option between 1 and 4.")

        print("--- Principal Menu ---")
        print("1. Check the credit cards list")
        print("2. Write the credit card you have")
        print(
            "3. Calculate the colombian points amount you would receive if you spend money"
        )
        print("4. Salir")

        option = int(input("Choose an option betwwen 1 and 4: "))


main()
