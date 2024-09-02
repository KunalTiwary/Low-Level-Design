from ..Adapter.WeightMachineAdapterImpl import WeightMachineAdapterImpl
from ..Adaptee.WeightMachineForBabiesImpl import WeightMachineForBabiesImpl


weightMachineAdapter = WeightMachineAdapterImpl(WeightMachineForBabiesImpl())
print(weightMachineAdapter.getWeightInKg())