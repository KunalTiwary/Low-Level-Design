from abc import ABC, abstractmethod


class WeightMachineAdapter(ABC):
    @abstractmethod
    def getWeightInKg(self):
        pass