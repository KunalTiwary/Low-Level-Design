from .VendingStates.State import State
from VendingStates.impl.IdleState import IdleState
from Inventory import Inventory

class VendingMachine:
    def __init__(self) -> None:
        self.state : State = IdleState()
        self.Inventory = Inventory(10)
        self.coinList = []

    def getState(self):
        return self.state

    def setState(self, state: State):
        self.state = state

    def getInventory(self):
        return self.Inventory

    def setInventory(self, inventory: Inventory):
        self.Inventory = inventory

    def getCoinList(self):
        return self.coinList

    def setCoinList(self, coinList):
        self.coinList = coinList