from abc import ABC, abstractmethod


class WeightMachine(ABC):
    @abstractmethod
    def getWeightInPounds(self):
        pass