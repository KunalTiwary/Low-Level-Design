from .HumanoidRobot import HumanoidRobot
from .RoboticDog import RoboticDog


class RobotFactory:
    def __init__(self):
        self.roboticMap = {}

    def createRobot(self, roboType):
        if roboType in self.roboticMap:
            return self.roboticMap[roboType]

        newRobot = HumanoidRobot(roboType, "HumanoidSprite")
        self.roboticMap[roboType] = newRobot
        return newRobot

