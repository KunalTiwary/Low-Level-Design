from .Shape import Shape
from .Color import Color


class Rectangle(Shape):
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        print("Drawing a rectangle")
        self.color.fill()