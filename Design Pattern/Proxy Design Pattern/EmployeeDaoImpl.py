from .EmployeeDo import EmployeeDo
from .EmployeeDao import EmployeeDao


class EmployeeDaoImpl(EmployeeDao):
    def create(self, client, ed: EmployeeDo) -> None:
        print("created new row")

    def delete(self, client, employeedo: EmployeeDo) -> None:
        print("deleted one row")

    def get(self, client, employeeId) -> EmployeeDo:
        print("fetching data")
        return EmployeeDo()

