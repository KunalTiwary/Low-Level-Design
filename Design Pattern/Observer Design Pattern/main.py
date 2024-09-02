from .Observable.IphoneObservable import IphoneObservable
from .Observable.BagObservable import BagObservable
from .Observer.MobileAlertObserver import MobileAlertObserver
from .Observer.EmailAlertObserver import EmailAlertObserver

if __name__ == "__main__":
    iphoneObservable = IphoneObservable()
    bagObservable = BagObservable()

    ob1 = MobileAlertObserver("98932", bagObservable)
    ob2 = EmailAlertObserver("xyz@gmail.com", iphoneObservable)

    iphoneObservable.add(ob1)
    iphoneObservable.add(ob2)
    bagObservable.add(ob1)

    iphoneObservable.setStockCount(10)
    bagObservable.setStockCount(20)

# you can run this by - python3 -m "Observer Design Pattern.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.
