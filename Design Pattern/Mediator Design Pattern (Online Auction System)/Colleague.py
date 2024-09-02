from abc import ABC, abstractmethod


class Colleague(ABC):
    @abstractmethod
    def placeBid(self, amount):
        pass

    @abstractmethod
    def receiveBidNotification(self, amount):
        pass

    @abstractmethod
    def getName(self):
        pass