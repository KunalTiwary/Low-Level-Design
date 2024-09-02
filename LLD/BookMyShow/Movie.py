class Movie:
    def __init__(self, movie_id, movie_name, movie_duration_in_minutes):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._movie_duration_in_minutes = movie_duration_in_minutes

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        self._movie_id = movie_id

    @property
    def movie_name(self):
        return self._movie_name

    @movie_name.setter
    def movie_name(self, movie_name):
        self._movie_name = movie_name

    @property
    def movie_duration_in_minutes(self):
        return self._movie_duration_in_minutes

    @movie_duration_in_minutes.setter
    def movie_duration_in_minutes(self, movie_duration):
        self._movie_duration_in_minutes = movie_duration
