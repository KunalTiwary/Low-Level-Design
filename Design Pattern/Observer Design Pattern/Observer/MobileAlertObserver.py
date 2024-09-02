from .NotificationAlertObserver import NotificationAlertObserver
from ..Observable.StocksObservable import StocksObservable


class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, contactNumber, stocksObservable: StocksObservable):
        self.contactNumber = contactNumber
        self.stocksObservable = stocksObservable

    def update(self, product):
        print(f'Hello, The stock of {product} is here - {self.contactNumber}')


