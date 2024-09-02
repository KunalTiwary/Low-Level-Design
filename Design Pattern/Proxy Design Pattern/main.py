from .EmployeeDaoProxy import EmployeeDaoProxy
from .EmployeeDo import EmployeeDo


if __name__ == "__main__":
    employeeTableObj = EmployeeDaoProxy()
    employeeTableObj.create("USER", EmployeeDo())
    print("success")

# you can run this by - python -m "Proxy Design Pattern.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.
