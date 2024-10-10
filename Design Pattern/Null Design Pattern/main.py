from .VehicleFactory import VehicleFactory

vehicleFactory = VehicleFactory()
vehicleObject = vehicleFactory.getVehicleObject("CAR")
print(vehicleObject.fuelCapacity())
print(vehicleObject.seatingCapacity())