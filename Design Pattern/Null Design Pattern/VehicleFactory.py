from .Car import Car
from .Null import Null


class VehicleFactory:
    def getVehicleObject(self, vehicleType):
        if vehicleType == "CAR":
            return Car()
        return Null()
