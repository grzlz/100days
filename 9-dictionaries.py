# Auction bidder
from os import system

# Create an empty list of bids

bids = []

# Create a function that stores name and bid
def bidder(name, bid):
    new_bidder = {
        "name": name,
        "bid": bid
    }

    bids.append(new_bidder)

# Create a function that returns the name and bid of the highest bid
def get_highest_bid(bids_list):
    
    highest_bidder = bids_list[0]["name"]
    highest_bid = bids_list[0]["bid"]

    for bid in bids_list:
        if bid["bid"] > highest_bid:
            highest_bid = bid["bid"]
            highest_bidder = bid["name"]

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



get_highest_bid(bids)

