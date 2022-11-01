import random
import deposit_def
import get_bet_def

def losowanie():
    """Random function free rows/columns"""
    lista_1 = []
    lista_2 = []
    lista_3 = []

    for i in range(3):
        lista_1.append(random.randint(1, 3))
        lista_2.append(random.randint(1, 3))
        lista_3.append(random.randint(1, 3))
    
    return lista_1, lista_2, lista_3

def main():
    """Main function"""
    new_amount = deposit_def.deposit()
    while True:
        
        new_bet = get_bet_def.get_bet()

        if new_bet <= new_amount:

            los_1, los_2, los_3 = losowanie()
            print(los_1)
            print(los_2)
            print(los_3)

            if los_1.count(los_1[0]) == 3 or los_2.count(los_2[0]) == 3 or los_3.count(los_3[0]) == 3:
                new_amount += new_bet
                print("Wygrales!!!")
                print(f"Twoja kwota to: {new_amount}")
            else:
                print("Niestety, ale przegrałaś :(")
                new_amount -= new_bet
                print(f"Twoja kwota to: {new_amount}")

                if new_amount == 0:
                    print("Dziękuje za gre :)")
                    break
        else:
            print("Podałeś za dużą kwote :P")

main()


