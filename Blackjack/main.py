from pydoc import safeimport

import art
import random

def card_deal(total):
    """Output a card value of 1-11. If the input + card value of 11 is more than 21, a card value of 1 is returned instead"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_output = 0
    if (random.choice(cards)) == 11 and (total + 11 > 21):
        card_output = 1
        return card_output
    else:
        card_output = random.choice(cards)
        return card_output

user_total = 0
dealer_total = 0
user_hand = []
dealer_hand = []
continue_game = 'y'

while (user_total <= 21 or dealer_total <= 21) and continue_game == 'y':

    another_card = 'y'

    if input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n' :") == continue_game:

        user_total = 0
        dealer_total = 0
        user_hand = []
        dealer_hand = []

        print(art.logo)

        user_hand.append(card_deal(user_total))
        user_hand.append(card_deal(user_total))
        user_total = sum(user_hand)
        dealer_hand.append(card_deal(dealer_total))

        print(f"Your cards: {user_hand}, current score: {user_total}")
        print(f"Dealer's fist card: {dealer_hand}")


        while user_total <= 21 and input("\nType 'y' to get another card, type 'n' to pass:\n ") == another_card:
            user_hand.append(card_deal(user_total))
            user_total = sum(user_hand)
            print(f"\nYour cards: {user_hand}, current score: {user_total}")
            print(f"Dealer's fist card: {dealer_hand}")

            if user_total > 21:
                print(f"\nYou went over! You lose")

            elif (user_total < dealer_total) and  (user_total <= 21):
                print(f"\nYou lose!")

        else:
            if user_total <= 21:
                print(f"\nYour final hand: {user_hand}, final score: {user_total}")

                while sum(dealer_hand) < 17:
                    dealer_hand.append(card_deal(dealer_total))
                    dealer_total = sum(dealer_hand)

                print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_total}")

                if dealer_total > 21:
                    print(f"\nDealer went over! You win!")

                elif (user_total > dealer_total):
                    print(f"\nYou win!")

                elif (user_total < dealer_total):
                    print(f"\nYou lose!")

                elif (user_total == dealer_total):
                    print(f"\nYou Draw")

    else:
        continue_game = 'n'
        print(f"Thanks for playing")



