from .ArithmeticExpression import ArithmeticExpression
from .Number import Number
from .OperationEnum import Operation
from .Expression import Expression


two = Number(2)
one = Number(1)
seven = Number(7)
addExpression = Expression(one, seven, Operation.ADD)
parentExpression = Expression(two, addExpression, Operation.MULTIPLY)
print(parentExpression.evaluate())
