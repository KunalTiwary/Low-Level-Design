from VendingStates.State import State
from VendingMachine import *
from Coin import *
from Item import *
from SelectionState import *
from IdleState import *


class HasMoneyState(State):
    def __init__(self) -> None:
        print("Currently Vending machine is in HasMoneyState")


    def clickOnInsertCoinButton(self, machine: VendingMachine) -> None:
        print("Vending machine is in HasMoneyState")


    def clickOnStartProductSelectionButton(self, machine: VendingMachine) -> None:
        machine.setState(SelectionState())
        pass


    def insertCoin(self, machine: VendingMachine, coin: Coin) -> None:
        print("Accepting Coin")
        machine.getCoinList().append(coin)
        pass 


    def chooseProduct(machine: VendingMachine, codeNumber: int) -> None:
        pass


    def getChange(self, returnChangeMoney: int) -> int:
        print("Vending machine is in HasMoneyState")
        pass


    def dispenseProduct(self, machine: VendingMachine, codeNumber: int) -> Item:
        print("Vending machine is in HasMoneyState")
        pass


    def refundFullMoney(self, machine: VendingMachine) -> list:
        print("Refunding the money")
        machine.setState(IdleState())
        return machine.getCoinList()


    def updateInventory(self, machine: VendingMachine, item: Item, codeNumber: int) -> None:
        machine.Inventory.addItem(codeNumber, item)
        pass
    