from .DriveStrategy import DriveStrategy



class SpecialDriveStrategy(DriveStrategy):
    def drive(self) -> None:
        print("Driving Specially")
