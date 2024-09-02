from .Shape import Shape
from .Color import Color


class Circle(Shape):
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        print("Drawing a circle")
        self.color.fill()