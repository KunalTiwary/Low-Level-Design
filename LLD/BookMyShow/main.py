from .Movie import Movie
from .MovieController import MovieController
from .Enum.City import City
from .TheatreController import TheatreController
from .Seat import Seat
from .Enum.SeatCategory import SeatCategory
from .Show import Show
from .Screen import Screen
from .Theatre import Theatre
from .Booking import Booking
from .Payment import Payment


if __name__ == "__main__":
    movieController = MovieController()
    theatreController = TheatreController()

    def createBooking(city: City, movieName, seatCategory: SeatCategory, numberOfSeats):
        print("Welcome to Book My show")
        movies = movieController.getMovieByCity(city)
        interestedMovie = ""
        for m in movies:
            if m.movie_name == movieName:
                interestedMovie = m
        if not interestedMovie:
            print("No such movie exists")
        shows = theatreController.getAllShows(interestedMovie, City.BANGALORE)
        interestedShow = ""
        for theatre, show in shows.items():
            if show[0].movie == interestedMovie:
                interestedShow = show[0]
        if not interestedShow:
            print("The interested movie has no shows")
        allSeats = interestedShow.screen.seats
        bookedSeats = interestedShow.bookedSeat
        interestedSeat = []
        for s in allSeats:
            if numberOfSeats == 0:
                break
            if s.category == seatCategory and s not in bookedSeats:
                interestedSeat.append(s)
                numberOfSeats -= 1
        if not interestedSeat:
            print("No seat found")
        booking = Booking(interestedShow, bookedSeats, Payment(1))
        for i in interestedSeat:
            interestedShow.bookedSeat.add(i)
        print(interestedShow.bookedSeat)
        print("Booking Successful")


    def initialize():
        createMovies()
        createTheatres()
        createBooking(City.BANGALORE, "Avengers", SeatCategory.PLATINUM, 2)
        pass

    def createMovies():
        bahubaliMovie = Movie(1, "Bahubali", 140)
        avengersMovie = Movie(2, "Avengers", 120)
        movieController.addMovie(bahubaliMovie, City.BANGALORE)
        movieController.addMovie(avengersMovie, City.BANGALORE)
        movieController.addMovie(bahubaliMovie, City.DELHI)
        movieController.addMovie(avengersMovie, City.DELHI)


    def createTheatres():
        seatList = createSeats()
        inoxTheatre = Theatre(1, "Karnataka", City.BANGALORE)
        inoxTheatre.screen = createScreens(seatList, 1)
        morningShow = createShows(inoxTheatre.screen[0], 1, movieController.getMovieByName("Bahubali"))
        eveningShow = createShows(inoxTheatre.screen[0], 2, movieController.getMovieByName("Avengers"))
        inoxTheatre.shows = [morningShow, eveningShow]

        pvrTheatre = Theatre(2, "Delhi", City.DELHI)
        pvrTheatre.screen = createScreens(seatList, 2)
        morningShow = createShows(pvrTheatre.screen[0], 1, movieController.getMovieByName("Bahubali"))
        eveningShow = createShows(pvrTheatre.screen[0], 2, movieController.getMovieByName("Avengers"))
        pvrTheatre.shows = [morningShow, eveningShow]

        theatreController.addTheatre(inoxTheatre, City.BANGALORE)
        theatreController.addTheatre(pvrTheatre, City.DELHI)

    def createSeats():
        seatList = []
        for i in range(1, 20):
            seat = Seat(i, 1, SeatCategory.SILVER)
            seatList.append(seat)

        for j in range(20, 40):
            seat = Seat(j, 2, SeatCategory.GOLD)
            seatList.append(seat)

        for k in range(40, 60):
            seat = Seat(k, 3, SeatCategory.PLATINUM)
            seatList.append(seat)
        return seatList

    def createScreens(seatList, id):
        screen = Screen(id)
        screen.seats = seatList
        return [screen]

    def createShows(screen, id, movie):
        show = Show(id, movie, screen)
        return show

    initialize()

