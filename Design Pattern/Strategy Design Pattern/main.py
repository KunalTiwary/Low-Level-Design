from GoodsVehicle import GoodsVehicle
from SportsVehicle import SportsVehicle


if __name__ == "__main__":
    goodsVehicle = GoodsVehicle()
    goodsVehicle.perform_drive()
    portsVehicle = SportsVehicle()
    portsVehicle.perform_drive()


# you can run this by - python -m "Strategy Design Pattern.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.
