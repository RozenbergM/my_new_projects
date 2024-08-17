bids = {}


def betting():
    name = input("What is your name?\n").lower()
    price = int(input("What is your bet?\n"))

    bids[name] = price

    finish_or_not = input('Any one wants to bet? Type "Yes" or "No":\n').lower()

    if finish_or_not == "yes":
        print("\n"*10)
        betting()
    elif finish_or_not == "no":
        winner = ""
        highest_bid = 0
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bids[bidder]
                winner = bidder

        print("\n" * 10)
        print(f"The Winner is {winner} with a bid of ${highest_bid}")


betting()
