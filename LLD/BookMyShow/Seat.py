from .Enum.SeatCategory import SeatCategory


class Seat:
    def __init__(self, seatId, row, category: SeatCategory):
        self.seatId = seatId
        self.row = row
        self.category = category

    @property
    def seatId(self):
        return self.seatId

    @seatId.setter
    def seatId(self, seatId):
        self._seatId = seatId

    @property
    def row(self):
        return self.row

    @row.setter
    def row(self, row):
        self._row = row

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category
