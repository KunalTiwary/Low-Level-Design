from abc import ABC, abstractmethod

from VendingMachine import *
from Coin import *
from Item import *

class State(ABC):

    @abstractmethod
    def clickOnInsertCoinButton(self, machine: 'VendingMachine') -> None:
        pass

    @abstractmethod
    def clickOnStartProductSelectionButton(self, machine: 'VendingMachine') -> None:
        pass

    @abstractmethod
    def insertCoin(self, machine: 'VendingMachine', coin: 'Coin') -> None:
        pass 

    @abstractmethod
    def chooseProduct(self, machine: 'VendingMachine', codeNumber: int) -> None:
        pass

    @abstractmethod
    def getChange(self, returnChangeMoney: int) -> int:
        pass

    @abstractmethod
    def dispenseProduct(self, machine: 'VendingMachine', codeNumber: int) -> 'Item':
        pass

    @abstractmethod
    def refundFullMoney(self, machine: 'VendingMachine') -> list:
        pass

    @abstractmethod
    def updateInventory(self, machine: 'VendingMachine', item: 'Item', codeNumber: int) -> None:
        pass