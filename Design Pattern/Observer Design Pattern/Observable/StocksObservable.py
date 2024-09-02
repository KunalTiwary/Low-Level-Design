from abc import ABC, abstractmethod
from ..Observer.NotificationAlertObserver import NotificationAlertObserver


class StocksObservable(ABC):

    @abstractmethod
    def add(self, observer: NotificationAlertObserver):
        pass

    @abstractmethod
    def remove(self, observer: NotificationAlertObserver):
        pass

    @abstractmethod
    def notifySubscribers(self):
        pass

    @abstractmethod
    def setStockCount(self, newStockAdded):
        pass

    @abstractmethod
    def getStockCount(self):
        pass
