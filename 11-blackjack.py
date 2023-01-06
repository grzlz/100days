# Create a black jack game
from random import choice


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

greeting = input("Welcome! Do you want to play blackjack? ")

# Create a function called pick  two cards

def initial_cards():
    user_cards = [choice(cards) for i in range(2)]

    return user_cards

def next_card():
    card = choice(cards)

    return card


def check_for_winner(user_cards, dealer_cards, compare_cards):
    user_sum = sum(user_cards)
    dealer_sum = sum(dealer_cards)

    if user_sum == 21 and dealer_sum == 21:
        return "It's a draw!"

    elif user_sum == 21:
        return "You won!"

    elif dealer_sum == 21:
        return "Dealer won!"

    elif user_sum > 21:
        return f"Your count is {user_sum}. You lost!"

    elif compare_cards:
        if user_sum > dealer_sum:
            return f"Your sum is {user_sum}, dealer's sum is {dealer_sum}. You won!"

        else:
            return f"Your sum is {user_sum}, dealer's sum is {dealer_sum}. Dealer won!"

    else: 
        return f"Your current count is {user_sum}"



if greeting == 'y':

    user_cards = initial_cards()
    dealer_cards = initial_cards()
    compare_cards = False

    print(f"Your cards are {user_cards}\nDealer's first card is {dealer_cards[0]}.")

    print(check_for_winner(user_cards, dealer_cards, compare_cards))

    continue_playing = input("Do you want another card? ")

    if continue_playing == "y":
    
        while compare_cards is not True:

            user_cards.append(next_card())

            if sum(user_cards) > 21:
                print(check_for_winner(user_cards, dealer_cards, compare_cards))
                break

            print(check_for_winner(user_cards, dealer_cards, compare_cards))

            if input("Do you want another card? ") == "n":
                compare_cards = True
                print(check_for_winner(user_cards, dealer_cards, compare_cards))

    elif continue_playing == "n":
        compare_cards = True
        print(check_for_winner(user_cards, dealer_cards, compare_cards))