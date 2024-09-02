from .FarmHouse import FarmHouse
from .Margherita import Margherita
from .VegDelight import VegDelight
from .Toppings.ExtraCheese import ExtraCheese
from .Toppings.Mushroom import Mushroom

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":

    p1 = FarmHouse()
    p2 = ExtraCheese(FarmHouse())
    p3 = Mushroom(ExtraCheese(VegDelight()))
    p4 = ExtraCheese(Margherita())

    print(p1.cost(), p2.cost(), p3.cost(), p4.cost())


# you can run this by - python -m "{main File Name}.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.

