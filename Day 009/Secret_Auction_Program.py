# Blind-auction-start 

logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\,
                         `'-------'`
                       .-------------.
                      /_______________\,

"""


import os
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bidden_record = {"Vicky" : 123, "kumar","321"}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print("The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    should_countinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_countinue == True:
        find_highest_bidder(bids)
    elif should_countinue == "yes":
        os.system('clear')
        



