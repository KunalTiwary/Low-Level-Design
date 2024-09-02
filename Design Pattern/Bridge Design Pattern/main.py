from .Circle import Circle
from .Red import Red
from .Rectangle import Rectangle
from .Blue import Blue


red_circle = Circle(Red())
blue_rectangle = Rectangle(Blue())

red_circle.draw()
blue_rectangle.draw()