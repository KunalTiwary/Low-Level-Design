from Item import *

class InventoryShelf:
    def __init__(self):
        self._code = None
        self._item = None
        self._sold_out = None

    def getCode(self):
        return self._code
    
    def setCode(self, code):
        self._code = code

    def getItem(self):
        return self._item

    def setItem(self, item:Item):
        self._item = item

    def getSoldOut(self):
        return self._sold_out

    def setSoldOut(self, soldOut:bool):
        self._sold_out = soldOut

    

    
        

