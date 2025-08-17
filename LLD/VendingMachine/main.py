from VendingMachine import VendingMachine
from Item import Item

def fill_up_inventory(vending_machine):
    slots = vending_machine.getInventory().getInventory()
    for i in range(len(slots)):
        new_item = Item()
        if 0 <= i < 3:
            new_item.setType("COKE")
            new_item.setPrice(12)
        elif 3 <= i < 5:
            new_item.setType("PEPSI")
            new_item.setPrice(9)
        elif 5 <= i < 7:
            new_item.setType("JUICE")
            new_item.setPrice(13)
        elif 7 <= i < 10:
            new_item.setType("SODA")
            new_item.setPrice(7)
        slots[i].setItem(new_item)
        slots[i].setSoldOut(False)

def display_inventory(vending_machine):
    slots = vending_machine.getInventory().getInventory()
    for i in range(len(slots)):
        code = slots[i].getCode()
        item = slots[i].getItem()
        item_type = item.getType() if item else "None"
        price = item.getPrice() if item else "None"
        is_available = not slots[i].getSoldOut()
        print(f"CodeNumber: {code} Item: {item_type} Price: {price} isAvailable: {is_available}")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    try:
        print("|")
        print("filling up the inventory")
        print("|")
        fill_up_inventory(vending_machine)
        display_inventory(vending_machine)
        print("|")
        print("clicking on InsertCoinButton")
        print("|")
        vending_state = vending_machine.getState()
        vending_state.clickOnInsertCoinButton(vending_machine)
        vending_state = vending_machine.getState()
        # Assuming Coin.NICKEL and Coin.QUARTER are available
        import Coin
        vending_state.insertCoin(vending_machine, Coin.NICKEL)
        vending_state.insertCoin(vending_machine, Coin.QUARTER)
        print("|")
        print("clicking on ProductSelectionButton")
        print("|")
        vending_state.clickOnStartProductSelectionButton(vending_machine)
        vending_state = vending_machine.getState()
        vending_state.chooseProduct(vending_machine, 102)
        display_inventory(vending_machine)
    except Exception as e:
        display_inventory(vending_machine)
