def get_bet():
    """The bet amount."""
    while True:
        amount = input("Podaj kwotę jaką chcesz zagrać: ")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount
            else:
                print("Podaj kwotę większą od 0!!!")
        else:
            print("Podana wartość jest błędna!!!")

    return int(amount)