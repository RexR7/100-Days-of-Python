# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def highest_bidder():
    max_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid = bidding_dict[bidder]
        if bid > max_bid:
            max_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${max_bid}.")

bidding_dict = {}
bidding_end = False
while not bidding_end:

    bidder_name = str(input("What is your name? "))
    bid_amount = int(input("What is your bid? $"))
    bidding_dict[bidder_name] = bid_amount

    other_user = str(input("Are there any other bidders? Type 'yes' or 'no'. ")).strip().lower()
    if other_user == "no":
        bidding_end = True
        highest_bidder()
    else:
        print("\n"*100)