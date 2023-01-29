# Ask user if they want to play the game of guess
# if the user says yes, print display message

# ask the user to choose difficulty level: easy or hard
# If the difficulty level is easy, num of attempts is 10, else num of attempts is 5
# Pick a number (random) between 1 and 100
# ask the user to enter their guess number

# Function to do the following:
# compare the guess number with the chosen number
# if the chosen number is greater print too high , ask for another guess, decrease the number of attempts
# if the chosen number is smaller, print too low, ask for another guess, decrease the number of attempts
# if the user guesses the correct number before they run out of trials, then end of game

# function to run the game
# If the user did not guess correct number, before the number of trials, then end of game, display the chosen number
import os
import random
from art import logo

EASY = 10
HARD = 5


def compare(number, guess):
    if guess > number:
        return "Too high"
    elif guess < number:
        return "Too low"
    else:
        return "Correct"


def guess():
    os.system('clear')
    play_game = input("Do you want to play the game of guess? type 'y' to play or type 'n' to quit: ")
    print(logo)
    if play_game == 'y':
        game()
    else:
        print("See You later!")


def game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
    computer_choice = random.randint(1, 100)
    print(f"Psst, the correct answer is {computer_choice}")
    difficulty_level = input("Choose a difficulty: Type 'easy' or 'Hard': ")
    num_attempts = EASY if difficulty_level == 'easy' else HARD

    game_over = False
    while not game_over:
        while num_attempts != 0:
            print(f"You have {num_attempts} attempts to guess the number")
            user_guess = int(input("Make a guess: "))
            result = compare(number=computer_choice, guess=user_guess)
            if result == "Correct":
                print(f"You got it. The answer was {computer_choice}")
                num_attempts = 0
            else:
                print(result)
                num_attempts -= 1
                if num_attempts == 0:
                    print("You've run out of guesses, you lose.")
        game_over = True


if __name__ == "__main__":
    guess()
