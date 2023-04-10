from art import logo, vs
from game_data import data
import random
import os


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account.get("name")
    description = account.get("description")
    country = account.get("country")
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    game_should_continue = True
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)} ")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a.get("follower_count")
        b_follower_count = account_b.get("follower_count")
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls')
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}. ")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    game()