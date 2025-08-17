from VendingStates.State import State
from VendingMachine import *
from Coin import *
from Item import *
from VendingStates.impl.HasMoneyState import HasMoneyState

class IdleState(State):
    def __init__(self):
        print("Currently Vending machine is in IdleState")

    def __init__(self, machine: VendingMachine) -> None:
        print("currently inside Idle State")
        machine.setCoinList([])


    def clickOnInsertCoinButton(self, machine: VendingMachine) -> None:
        machine.setState(HasMoneyState())
        pass


    def clickOnStartProductSelectionButton(self, machine: VendingMachine) -> None:
        print("Currently on Idle State")
        pass


    def insertCoin(self, machine: VendingMachine, coin: Coin) -> None:
        print("Currently on Idle State")
        pass 


    def chooseProduct(machine: VendingMachine, codeNumber: int) -> None:
        print("Currently on Idle State")
        pass


    def getChange(self, returnChangeMoney: int) -> int:
        print("Currently on Idle State")
        pass


    def dispenseProduct(self, machine: VendingMachine, codeNumber: int) -> Item:
        print("Currently on Idle State")
        pass


    def refundFullMoney(self, machine: VendingMachine) -> list:
        print("Currently on Idle State")
        pass
    

    def updateInventory(self, machine: VendingMachine, item: Item, codeNumber: int) -> None:
        machine.Inventory.addItem(codeNumber, item)
        pass