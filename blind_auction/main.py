import os

os.system('cls')

if __name__ == "__main__":
    name = input("What is your?: ")
    bid = int(input("What is your bid?: $"))
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    winner = ''
    winning_bid = ''
    print("The winner is {winner} with a bid of ${winning_bid}")
