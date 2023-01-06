# Create a black jack game
from random import choice


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

greeting = input("Welcome! Do you want to play blackjack? ")

# Create a function called pick  two cards

def initial_cards():
    user_cards = [choice(cards) for i in range(2)]

    return user_cards

if greeting == 'y':

    user_cards = initial_cards()
    dealer_cards = initial_cards()



    print(f"Your cards are {user_cards}. Dealer first card is {dealer_cards[0]}")
