from .Enum.City import City


class Theatre:
    def __init__(self, theatre_id: int, address: str, city: City):
        self._theatre_id = theatre_id
        self._address = address
        self._city = city
        self._screen = []
        self._shows = []

    # Getter and Setter for theatre_id
    @property
    def theatre_id(self):
        return self._theatre_id

    @theatre_id.setter
    def theatre_id(self, theatre_id):
        self._theatre_id = theatre_id

    # Getter and Setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    # Getter and Setter for screen
    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, screen):
        self._screen = screen

    # Getter and Setter for shows
    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, shows):
        self._shows = shows

    # Getter and Setter for city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: City):
        self._city = city
