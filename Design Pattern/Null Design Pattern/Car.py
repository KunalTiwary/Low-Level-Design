from .Vehicle import Vehicle


class Car(Vehicle):
    def seatingCapacity(self):
        return 5

    def fuelCapacity(self):
        return 40