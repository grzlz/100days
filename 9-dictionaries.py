# Auction bidder
from os import system

# Create an empty list of bids

bids_dict = {}

# Create a function that stores name and bid
def bidder(name, bid):
    bids_dict[name] = int(bid)

# Create a function that returns the name and bid of the highest bid
def get_highest_bid(bids_dict):
    
    highest_bidder = ""
    highest_bid = 0

    for bidder in bids_dict:
        if bids_dict[bidder] > highest_bid:
            highest_bid = bids_dict[bidder]
            highest_bidder = bidder

    print(f"The highest bidder is {highest_bidder} for ${highest_bid}.")


# Create a condition and loop while True
new_bid = True

while new_bid:
    new_name = input("What is your name? ")
    new_bid = int(input("What is your bid? $"))
    bidder(new_name, new_bid)

    if input("Are there more bidders? ") == "No":
        new_bid = False
    
    system("clear")
    print(bids_dict)




get_highest_bid(bids_dict)

