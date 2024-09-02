from .Command import Command
from .AC import AC


class SetTemperatureCommand(Command):
    def __init__(self, ac: AC, temperature: int):
        self.ac = ac
        self.temperature = temperature
        self.prev_temperature = None

    def execute(self):
        self.prev_temperature = getattr(self.ac, 'temperature', None)
        self.ac.set_temperature(self.temperature)

    def undo(self):
        if self.prev_temperature is not None:
            self.ac.set_temperature(self.prev_temperature)
