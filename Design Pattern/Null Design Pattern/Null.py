from .Vehicle import Vehicle


class Null(Vehicle):
    def seatingCapacity(self):
        return 0

    def fuelCapacity(self):
        return 0