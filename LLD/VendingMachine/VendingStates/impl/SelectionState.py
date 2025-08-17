from VendingStates.State import State
from VendingMachine import *
from Coin import *
from Item import *
from VendingStates.impl.DispenseState import *
from VendingStates.impl.IdleState import *


class SelectionState():
    def __init__(self) -> None:
        print("Currently Vending machine is in SelectionState")

    def clickOnInsertCoinButton(self, machine: VendingMachine) -> None:
        pass

    def clickOnStartProductSelectionButton(self, machine: VendingMachine) -> None:
        pass

    def insertCoin(self, machine: VendingMachine, coin: Coin) -> None:
        pass 

    def chooseProduct(machine: VendingMachine, codeNumber: int) -> None:
        try:
            item = machine.getInventory().getItem(codeNumber)
            paidByUser = 0

            for coin in machine.getCoinList():
                paidByUser += coin.value

            if paidByUser < item.getPrice():
                print(f"Insufficient Amount, Product you selected is for price: {item.getPrice()} and you paid: {paidByUser}")
                SelectionState().refundFullMoney(machine)
                raise Exception("insufficient amount")
            else:
                if paidByUser >= item.getPrice():
                    if paidByUser > item.getPrice():
                        SelectionState().getChange(paidByUser - item.getPrice())
                    machine.setState(DispenseState(machine, codeNumber))
        except Exception as e:
            print(str(e))       

    def getChange(self, returnChangeMoney: int) -> int:
        print("Returned the change in the Coin Dispense Tray: " + returnChangeMoney);
        return returnChangeMoney;

    def dispenseProduct(self, machine: VendingMachine, codeNumber: int) -> Item:
        pass

    def refundFullMoney(self, machine: VendingMachine) -> list:
        print("Refunding the money")
        machine.setState(IdleState())
        return machine.getCoinList()

    def updateInventory(self, machine: VendingMachine, item: Item, codeNumber: int) -> None:
        pass
