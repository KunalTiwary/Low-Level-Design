from abc import ABC, abstractmethod
from .Colleague import Colleague


class AuctionMediator(ABC):
    @abstractmethod
    def addBidder(self, bidder: Colleague):
        pass

    @abstractmethod
    def placeBid(self, bidder: Colleague, amount):
        pass