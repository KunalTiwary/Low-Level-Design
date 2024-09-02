from .ArithmeticExpression import ArithmeticExpression
from .OperationEnum import Operation


class Expression(ArithmeticExpression):
    def __init__(self, left: ArithmeticExpression, right: ArithmeticExpression, operation: Operation):
        self.left = left
        self.right = right
        self.operation = operation

    def evaluate(self):
        if self.operation == Operation.ADD:
            return self.left.evaluate() + self.right.evaluate()
        elif self.operation == Operation.SUBTRACT:
            return self.left.evaluate() - self.right.evaluate()
        elif self.operation == Operation.MULTIPLY:
            return self.left.evaluate() * self.right.evaluate()
        elif self.operation == Operation.DIVIDE:
            return self.left.evaluate() / self.right.evaluate()

