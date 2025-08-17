from ast import List
from InventoryShelf import InventoryShelf
from Item import Item


class Inventory:
    def __init__(self, itemCount:int) -> None:
        self.inventory  = [None] * itemCount
        self.setInitialInventory()

    def getInventory(self):
        return self.inventory

    def setInventory(self, inventory:List):
        self.inventory = inventory

    def setInitialInventory(self):
        startCode = 101

        for i in range(len(self.inventory)):
            space = InventoryShelf()
            self.inventory[i] = space
            space.setCode(startCode)
            space.getSoldOut(False)
            startCode += 1
    
    def addItem(self, codeNumber, item:Item):
        for i in range(len(self.inventory)):
            if self.inventory[i] and self.inventory[i].getCode() == codeNumber:
                iShelf : InventoryShelf = self.inventory[i]
                if iShelf.getSoldOut():
                    raise Exception("already item is present, you can not add item here")
                iShelf.setItem(item)
                iShelf.getSoldOut(False)


    def getItem(self, codeNumber):
        for i in range(len(self.inventory)):
            if self.inventory[i] and self.inventory[i].getCode() == codeNumber:
                iShelf : InventoryShelf = self.inventory[i]
                if iShelf.getSoldOut():
                    raise Exception("Item Sold Out")
        return iShelf.getItem()


    def updateSoldOut(self, codeNumber, soldOut):
        for i in range(len(self.inventory)):
            if self.inventory[i] and self.inventory[i].getCode() == codeNumber:
                iShelf : InventoryShelf = self.inventory[i]
                iShelf.setSoldOut() = soldOut
                return True
        raise Exception (f"Item with code number : {codeNumber} does not exist")
                

