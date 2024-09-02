from abc import ABC, abstractmethod
from .EmployeeDo import EmployeeDo


class EmployeeDao(ABC):
    @abstractmethod
    def create(self, client, ed: EmployeeDo) -> None:
        pass

    @abstractmethod
    def delete(self, client, employeedo: EmployeeDo) -> None:
        pass

    @abstractmethod
    def get(self, client, employeeId) -> EmployeeDo:
        pass