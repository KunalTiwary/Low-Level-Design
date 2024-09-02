from Vehicle import Vehicle
from Strategy.SpecialDriveStrategy import SpecialDriveStrategy


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())
