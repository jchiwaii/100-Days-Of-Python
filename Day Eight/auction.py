from ascii import logo
from os import system, name

print(logo)

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    if not isinstance(name, str):
        print("Error: Name must be a string.")
        continue
    try:
        price = int(input("What is your bid?: $"))
    except ValueError:
        print("Error: Bid must be a number.")
        continue
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue.lower() == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == 'yes':
        clear_screen()
