from VendingStates.State import State
from VendingMachine import *
from Coin import *
from Item import *
from IdleState import IdleState

class DispenseState(State):
    def __init__(self, machine: VendingMachine, codeNumber: int) -> None:
        print("Currently Vending machine is in DispenseState")
        self.dispenseProduct(machine, codeNumber)

    def clickOnInsertCoinButton(self, machine: VendingMachine) -> None:
        print("Vending machine is in DispenseState")

    def clickOnStartProductSelectionButton(self, machine: VendingMachine) -> None:
        print("Vending machine is in DispenseState")

    def insertCoin(self, machine: VendingMachine, coin: Coin) -> None:
        print("Vending machine is in DispenseState")

    def chooseProduct(self, machine: VendingMachine, codeNumber: int) -> None:
       print("Vending machine is in DispenseState")

    def getChange(self, returnChangeMoney: int) -> int:
        print("Vending machine is in DispenseState")

    def refundFullMoney(self, machine: VendingMachine) -> list:
        print("Vending machine is in DispenseState")

    def dispenseProduct(self, machine: VendingMachine, codeNumber: int) -> Item:
        print("Product has been dispensed")
        item = machine.getInventory().getItem(codeNumber)
        machine.getInventory().updateSoldOutItem(codeNumber)
        machine.setState(IdleState(machine))
        return item

    def updateInventory(self, machine: VendingMachine, item: Item, codeNumber: int) -> None:
        print("Vending machine is in DispenseState")
