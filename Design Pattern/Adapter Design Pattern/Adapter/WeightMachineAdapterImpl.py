from .WeightMachineAdapter import WeightMachineAdapter
from ..Adaptee.WeightMachine import WeightMachine


class WeightMachineAdapterImpl(WeightMachineAdapter):
    def __init__(self, w: WeightMachine):
        self.w = w

    def getWeightInKg(self):
        weightInPounds = self.w.getWeightInPounds()
        return weightInPounds * 0.25
