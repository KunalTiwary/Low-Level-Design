from .ComputerFacade import ComputerFacade


computer = ComputerFacade()
computer.start_computer()


# python3 -m "Facade Design Pattern.main"

# Diff between facade and proxy - 1) Proxy can create the object of only one class
# 2) Proxy is an implementation of the same abstract class

# Diff between facade and adapter - 1) Adapter pattern is used when the client and adaptee is incompatible whereas
# facade is used to hide the complexity
