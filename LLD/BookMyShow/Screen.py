from .Seat import Seat


class Screen:
    def __init__(self, screenId):
        self.screenId = screenId
        self.seats = []

    @property
    def screenId(self):
        return self.screenId

    @screenId.setter
    def screenId(self, value):
        self._screenId = value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value

    def getSeat(self, seatId):
        for s in self.seats:
            if s.seatId == seatId:
                return s
        return None

    








