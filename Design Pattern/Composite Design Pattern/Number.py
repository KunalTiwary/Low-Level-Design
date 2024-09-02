from .ArithmeticExpression import ArithmeticExpression


class Number(ArithmeticExpression):
    def __init__(self, num: int):
        self.num = num

    def evaluate(self):
        print(f"The number is {self.num}")
        return self.num
