############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

###############################################################
import os
from art import logo
import random
from emoji import emojize


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_in_hand):
    if (len(cards_in_hand) == 2) and (10 in cards_in_hand) and (11 in cards_in_hand):
        return 0
    elif 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)
    return sum(cards_in_hand)


def check_for_blackjack(user_score, computer_score):
    if user_score == 0 or computer_score == 0:
        if computer_score == 0:
            return "computer"
        elif user_score == 0:
            return "user"


def compare(user_score, computer_score):

    if computer_score > user_score:
        return "computer"
    elif user_score > computer_score:
        return "user"
    else:
        return "draw"


def play_blackjack():
    start_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start_game == 'y':
        os.system('cls')
        print(logo)
        computer_cards = [deal_card() for i in range(2)]
        user_cards = [deal_card() for i in range(2)]

        user_game = True
        while user_game:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print("Your Cards: ", user_cards, "current score: ", user_score)
            print("Computer's first card: ", computer_cards[0])

            # check for blackjack
            blackjack = check_for_blackjack(user_score, computer_score)
            if blackjack == 'computer':
                print("Computer's hand: ", computer_cards, "\nComputer has Blackjack. \nComputer Wins!",
                      emojize(":smiling_face_with_halo:"))
                user_game = False
            elif blackjack == 'user':
                print("You have Blackjack. You win!", emojize(
                    ":smiling_face_with_sunglasses:"))
                user_game = False
            elif user_score > 21:
                print("You went over. You lose! Better luck next time", emojize(":smiling_face_with_halo:"),
                      "\nComputer's Hand: ", computer_cards)
                user_game = False

            # Regular play
            else:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if another_card == 'y':
                    user_cards.append(deal_card())
                else:
                    while computer_score < 17:
                        computer_cards.append(deal_card())
                        computer_score = calculate_score(computer_cards)
                    winner = compare(user_score, computer_score)

                    if computer_score > 21:
                        print("The computer went over",
                              computer_cards, "You win!", emojize(":smiling_face_with_sunglasses:"))

                    elif winner == 'computer':
                        print("Computer's hand: ", computer_cards,
                              "\nComputer's hand is more than your hand\nComputer's score: ", computer_score, "\nComputer Wins!", emojize(":smiling_face_with_halo:"))

                    elif winner == 'user':
                        print("Computer's hand: ", computer_cards,
                              "\nYour hand is more than your computer's\nComputer's score: ", computer_score, "\nYou Win!",  emojize(":smiling_face_with_sunglasses:"))

                    elif winner == 'draw':
                        print("Computer's hand: ", computer_cards, "The game ends in a draw.", emojize(
                            ":unamused_face:"), "\nComputer's score: ", computer_score)
                    user_game = False

        play_blackjack()

    else:
        print("See you later!", emojize(":grinning_face:"))


if __name__ == "__main__":
    play_blackjack()
