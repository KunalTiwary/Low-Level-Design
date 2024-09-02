from .RobotFactory import RobotFactory


factory = RobotFactory()
robo1 = factory.createRobot("HUMANOID")
robo2 = factory.createRobot("DOG")

robo1.display(1,1)
robo1.display(1,2)
robo1.display(1,3)
robo1.display(1,4)

robo2.display(10,10)
robo2.display(10,9)
robo2.display(10,8)
robo2.display(10,7)
