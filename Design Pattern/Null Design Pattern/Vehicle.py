from abc import abstractmethod, ABC


class Vehicle(ABC):
    @abstractmethod
    def seatingCapacity(self):
        pass

    @abstractmethod
    def fuelCapacity(self):
        pass