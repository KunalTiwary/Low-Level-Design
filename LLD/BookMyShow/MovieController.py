from .Movie import Movie
from .Enum.City import City


class MovieController:
    def __init__(self):
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie: Movie, city: City):
        self.allMovies.append(movie)
        self.cityVsMovies[city] = self.cityVsMovies.get(city, [])
        self.cityVsMovies[city].append(movie)


    def getMovieByName(self, movieName):
        for m in self.allMovies:
            if m.movie_name == movieName:
                return m
        return None

    def getMovieByCity(self, city: City):
        return self.cityVsMovies[city] if city in self.cityVsMovies else None
