from .DriveStrategy import DriveStrategy


class NormalDriveStrategy(DriveStrategy):
    def drive(self) -> None:
        print("Driving Normally")
