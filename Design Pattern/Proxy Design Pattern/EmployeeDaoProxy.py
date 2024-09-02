from .EmployeeDao import EmployeeDao
from .EmployeeDaoImpl import EmployeeDaoImpl
from .EmployeeDo import EmployeeDo


class EmployeeDaoProxy(EmployeeDao):
    def __init__(self):
        self.employeeDaoImpl = EmployeeDaoImpl()

    def create(self, client, ed: EmployeeDo) -> None:
        if client == "ADMIN":
            return self.employeeDaoImpl.create(client, ed)
        print("Access denied")

    def delete(self, client, ed: EmployeeDo) -> None:
        if client == "ADMIN":
            return self.employeeDaoImpl.delete(client, ed)
        print("Access denied")

    def get(self, client, ed) -> EmployeeDo:
        if client == "ADMIN" or client == "USER":
            return self.employeeDaoImpl.get(client, ed)
        print("Access denied")

