import os
from art import logo

def collect_auction_data(name, bid):
    bid_details = {
        "name": name,
        "bidAmount": bid
    }
    auction_data.append(bid_details)


if __name__ == "__main__":
    print(logo)
    auction_data = []
    continue_auction = True
    while continue_auction:
        name = input("What is your Name?: ")
        bid = int(input("What is your bid?: $"))
        collect_auction_data(name, bid)
        next_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        os.system('cls')
        if next_bidder == 'no':
            continue_auction = False
            print("End of Auction!\n")
    
    highest_bidder = {}
    highest_amount = 0
    for item in auction_data:
        bid_amount = item["bidAmount"]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            highest_bidder = item

    highest_bidder_name = highest_bidder["name"]
    print(f"The winner is {highest_bidder_name} with a bid of ${highest_amount}")
