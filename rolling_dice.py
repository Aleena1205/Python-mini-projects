import random
def roll_dice():
    min_val=1
    max_val=6

    roll_again=True

    while roll_again:
        print("The number is:",random.randint(min_val,max_val))
        roll_again=input("Do you want to roll the dice again? (yes/no): ").lower() == "yes"

    print("Goodbye")


roll_dice()

        

          
