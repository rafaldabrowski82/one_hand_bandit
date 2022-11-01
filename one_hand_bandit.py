import random

import deposit_def
import get_bet_def
import random_lists

def main():
    """Main function"""
    new_amount = deposit_def.deposit()
    while True:
        
        new_bet = get_bet_def.get_bet()

        if new_bet <= new_amount:

            los_1, los_2, los_3 = random_lists.random_list()
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


