from Vehicle import Vehicle
from Strategy.SpecialDriveStrategy import SpecialDriveStrategy



class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())
