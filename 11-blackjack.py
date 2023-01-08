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



def check_for_winner(user_sum, dealer_sum):
    if user_sum == 21 and dealer_sum == 21:
        return 0

    elif user_sum == 21:
        return 1

    elif dealer_sum == 21:
        return 2

    elif user_sum > 21:
        return 3

    else: 
        return 4

def compare_cards():
    if user_sum == dealer_sum:
        return f"You got {user_sum} and the dealer {dealer_sum}. It's a draw!"

    elif user_sum > dealer_sum:
        return f"You got {user_sum} and the dealer {dealer_sum}. You won!"

    else:
        return f"You got {user_sum} and the dealer {dealer_sum}. You lose!"

if greeting == 'y':

    user_cards = initial_cards()
    dealer_cards = initial_cards()

    print(f"Your cards are {user_cards}\nDealer's first card is {dealer_cards[0]}.")

    user_sum = sum(user_cards)
    dealer_sum = sum(dealer_cards)

    print(f"Your current count is {user_sum}.")

    if user_sum == 21:
        print(f"Your cards are {user_cards}, dealers are {dealer_cards}.\n You scored {user_sum}. You won!")
        continue_playing = False

    else:
        continue_playing = input("Do you want another card? ")

        while continue_playing == "y":
            new_card = next_card()

            if new_card == 11 and user_sum + new_card > 21:
                new_card = 1

            user_cards.append(new_card)
            user_sum += new_card
            print(f"Your cards are {user_cards}")

            result = check_for_winner(user_sum, dealer_sum)

            if result == 0:
                print("It's a draw!")
                continue_playing = False

            elif result == 1:
                print("You won!")
                continue_playing = False

            elif result == 2:
                print("Dealer won!")
                continue_playing = False
            
            elif result == 3:
                print(f"Count is {user_sum}. You got busted! You lose.")
                continue_playing = False

            elif result == 4:
                print(f"Count is {user_sum}.")
                continue_playing = input("Do you want another card? ")

    if continue_playing == "n":
        result = compare_cards()
        print(result)

else: 
    print("Bye!")