from .AuctionMediator import AuctionMediator
from .Colleague import Colleague


class Auction(AuctionMediator):
    def __init__(self):
        self.colleagues = []

    def addBidder(self, bidder: Colleague):
        self.colleagues.append(bidder)

    def placeBid(self, bidder: Colleague, amount):
        for c in self.colleagues:
            if c.getName() != bidder.getName():
                c.receiveBidNotification(amount)
