import os
from art import logo

print(logo)
print("Welcome to the Blind Bid Auction program.")

bidders = {}
more_bidders = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        user_bid = bidding_record[bidder]
        if user_bid > highest_bid:
            winner = bidder
            highest_bid = user_bid

    print(f"The winner is {winner} with a bid of $ {'{:.2f}'.format(highest_bid)}")


while more_bidders:
    name = input("What is your name?:  ")
    bid = float(input("What is your bid?: $ "))
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if add_bidder == "no":
        more_bidders = False
    else:
        # Clear the console prior to another loop, adjusting the command to either Windows or Linux OS
        # It doesn't work within PyCharm console
        os.system('cls' if os.name == 'nt' else 'clear')
    bidders[name] = bid

find_highest_bidder(bidders)
