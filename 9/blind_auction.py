import os


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def gather_bids():
    bids = {}
    keep_running = True
    while keep_running:
        name = input("What's your name?\n")
        amount = int(input("How much are you willing to pay?\n$"))
        bids[name] = amount
        to_continue = input(
            "Are there other people that are willing to participate? Type 'yes' or 'no'.\n").lower().strip()
        if to_continue == "no":
            keep_running = False
        clear()
    return bids


def main():
    bids = gather_bids()
    highest_bid = max(bids.values())
    for name, bid in bids.items():
        if bid == highest_bid:
            print("Auction winner: {} with a bid of ${}!".format(name, bid))


if __name__ == "__main__":
    main()
