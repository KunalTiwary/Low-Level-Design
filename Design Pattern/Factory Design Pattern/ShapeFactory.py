from Circle import Circle
from Rectangle import Rectangle


class ShapeFactory:
    def __init__(self):
        self.figure = "Circle"

    def getShape(self):
        if self.figure == "Circle":
            return Circle()
        else:
            return Rectangle()

