import os
import random
from art import logo

EASY = 10
HARD = 5


def compare(number, guess_number):
    if guess_number > number:
        return "Too high"
    elif guess_number < number:
        return "Too low"
    else:
        return "Correct"


def guess():
    play_game = input("Do you want to play the game of guess? type 'y' to play or type 'n' to quit: ")
    os.system('clear')
    print(logo)
    if play_game == 'y':
        game()
    else:
        print("See You later!")


def game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
    computer_choice = random.randint(1, 100)
    # print(f"Psst, the correct answer is {computer_choice}")
    difficulty_level = input("Choose a difficulty: Type 'easy' or 'Hard': ")
    num_attempts = EASY if difficulty_level == 'easy' else HARD

    while num_attempts != 0:
        print(f"You have {num_attempts} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        result = compare(number=computer_choice, guess_number=user_guess)
        if result == "Correct":
            print(f"You got it. The answer was {computer_choice}")
            num_attempts = 0
        else:
            print(result)
            num_attempts -= 1
            if num_attempts == 0:
                print("You've run out of guesses, you lose.")
    guess()


if __name__ == "__main__":
    guess()
