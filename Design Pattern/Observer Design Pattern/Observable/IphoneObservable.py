
from .StocksObservable import StocksObservable
from ..Observer.NotificationAlertObserver import NotificationAlertObserver

class IphoneObservable(StocksObservable):
    def __init__(self):
        self.ObserverList = set()
        self.stockCount = 0
        self.product = "Iphone"

    def add(self, observer: NotificationAlertObserver):
        self.ObserverList.add(observer)

    def remove(self, observer: NotificationAlertObserver):
        self.ObserverList.remove(observer)

    def notifySubscribers(self):
        for observer in self.ObserverList:
            observer.update(self.product)

    def setStockCount(self, newStockAdded):
        if self.stockCount == 0:
            self.notifySubscribers()
        self.stockCount += newStockAdded

    def getStockCount(self):
        return self.stockCount
