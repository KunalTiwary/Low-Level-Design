from .Command import Command
from .AC import AC


class TurnOnCommand(Command):
    def __init__(self, ac: AC):
        self.ac = ac

    def execute(self):
        self.ac.turn_on()

    def undo(self):
        self.ac.turn_off()
