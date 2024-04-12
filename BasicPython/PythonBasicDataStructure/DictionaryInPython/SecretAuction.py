import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


auctionContinue = True
auction = {}

# def highestBidder(BiddingRecord):
#     highestBid = 0
#     winner = ''
#     for bid in BiddingRecord:
#         bidAmount = BiddingRecord[bid]
#         if bidAmount > highestBid:
#             highestBid = bidAmount
#             winner = bid
#     print(f'The winner is {winner} with a bid of ${highestBid}')


while auctionContinue:
    name = input('enter the name :')
    bids = int(input('enter the Bid price: '))
    auction[name] = bids
    print(auction)
    another = input("IS there  any other user? say 'Yes' to be continue or 'No to quit: ").lower()
    if another == 'yes':
        auctionContinue = True
        clear_screen()
    else:
        auctionContinue = False
        highestBid = 0
        winner = ''
        for bid in auction:
            valueBid = auction[bid]
            if valueBid > highestBid:
                highestBid = valueBid
                winner = bid
        print(f'The winner is {winner} with a bid of ${highestBid}')

print(auction)
