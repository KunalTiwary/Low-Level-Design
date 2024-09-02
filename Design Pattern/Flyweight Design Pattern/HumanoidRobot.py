from .Robot import Robot


class HumanoidRobot(Robot):
    def __init__(self, roboType, body):
        self._type = roboType
        self._body = body

    def getType(self):
        return self._type

    def getBody(self):
        return self._body

    def display(self, x, y):
        # display a robot
        pass
