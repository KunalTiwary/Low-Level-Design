from .Theatre import Theatre
from .Movie import Movie
from .Enum.City import City

class TheatreController:
    def __init__(self):
        self.cityVsTheatres = {}
        self.allTheatres = []

    def addTheatre(self, theatre: Theatre, city: City):
        self.allTheatres.append(theatre)
        self.cityVsTheatres[city] = self.cityVsTheatres.get(city, [])
        self.cityVsTheatres[city].append(theatre)

    def getAllShows(self, movie: Movie, city):
        theatreVsShows = {}
        theatres = self.cityVsTheatres.get(city)
        allShowsInCityWithSameMovie = []
        for t in theatres:
            shows = t.shows
            for show in shows:
                if show.movie.movie_id == movie.movie_id:
                    allShowsInCityWithSameMovie.append(show)
            if allShowsInCityWithSameMovie:
                theatreVsShows[t] = allShowsInCityWithSameMovie
        return theatreVsShows
