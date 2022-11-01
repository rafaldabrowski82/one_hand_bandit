def deposit():
    """The amount which user start the game"""
    while True:
        amount = input("Podaj kwotę początkową: ")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount
            else:
                print("Podaj kwotę większą od 0!!!")
        else:
            print("Podana wartość jest błędna!!!")

    return int(amount)