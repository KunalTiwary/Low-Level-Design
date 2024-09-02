from .CPU import CPU
from .Memory import Memory
from .HardDrive import HardDrive


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("ComputerFacade: Starting computer")
        self.cpu.freeze()
        boot_data = self.hard_drive.read("Sector 0", 512)
        self.memory.load("0x00", boot_data)
        self.cpu.jump("0x00")
        self.cpu.execute()