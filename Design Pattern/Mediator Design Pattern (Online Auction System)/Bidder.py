from .Colleague import Colleague
from .AuctionMediator import AuctionMediator


class Bidder(Colleague):
    def __init__(self, name, auctionMediator: AuctionMediator):
        self.name = name
        self.auctionMediator = auctionMediator
        self.auctionMediator.addBidder(self)

    def placeBid(self, amount):
        self.auctionMediator.placeBid(self, amount)

    def receiveBidNotification(self, amount):
        print(f"Notification Received - {self.name}, Amount - {amount}")

    def getName(self):
        return self.name
