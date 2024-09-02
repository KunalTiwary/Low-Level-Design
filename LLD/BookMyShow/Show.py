from .Movie import Movie
from .Seat import Seat
from .Screen import Screen


class Show:
    def __init__(self, showId, movie: Movie, screen: Screen):
        self.showId = showId
        self.movie = movie
        self.screen = screen
        self._bookedSeat = set()

    @property
    def showId(self):
        return self.showId

    @showId.setter
    def showId(self, value):
        self._showId = value

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        self._movie = value

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    @property
    def bookedSeat(self):
        return self._bookedSeat

    @bookedSeat.setter
    def bookedSeat(self, value):
        self._bookedSeat.add(value)
