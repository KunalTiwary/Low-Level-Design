from .Show import Show


class Booking:
    def __init__(self, show: Show, booked_seats, payment):
        self._show = show
        self._booked_seats = booked_seats if booked_seats is not None else []
        self._payment = payment

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, show):
        self._show = show

    @property
    def booked_seats(self):
        return self._booked_seats

    @booked_seats.setter
    def booked_seats(self, booked_seats):
        self._booked_seats = booked_seats

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, payment):
        self._payment = payment
