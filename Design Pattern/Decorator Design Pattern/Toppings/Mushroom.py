from .ToppingDecorator import ToppingDecorator
from ..BasePizza import BasePizza


class Mushroom(ToppingDecorator):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + 10
