import os
from art import logo

print(logo)
print("Welcome to the secret Auction program.")


def clear_console():
    os.system('cls')


keep_biding = True
bidders = {}
while keep_biding:
    name = input("What is your name? ")
    bid = int(input("What is you bid? $"))

    bidders[name] = bid
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
 
    highest_bid = 0

    if more_bidders == "no":
        for name in bidders:
            bid_amount = bidders[name]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = name
        print(f"The winner is {name} with a bid of ${highest_bid}")
        keep_biding = False
    elif more_bidders == "yes":
        clear_console()


