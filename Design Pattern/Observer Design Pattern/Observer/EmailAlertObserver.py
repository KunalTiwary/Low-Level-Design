from .NotificationAlertObserver import NotificationAlertObserver
from ..Observable.StocksObservable import StocksObservable


class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, emailId, stocksObservable: StocksObservable):
        self.emailId = emailId
        self.stocksObservable = stocksObservable

    def update(self, product):
        print(f'Hello, The stock of {product} is here - {self.emailId}')