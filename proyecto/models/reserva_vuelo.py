from models.vuelo import Vuelo
from models.reserva import Reserva

class ReservaVuelo(Reserva):
    def _init_(self, idReserva, fechaReserva, estado, turista, sucursal, monto,
                 vuelo: Vuelo, numPasajeros: int, asientos: str, clase: str):
        super()._init_(idReserva, fechaReserva, estado, turista, sucursal, monto)
        self.__vuelo = vuelo
        self.__numPasajeros = numPasajeros
        self.__asientos = asientos
        self.__clase = clase

    def validarDispo(self):
        return self.__vuelo.consultarDisponibilidad()

    def confirmarReserva(self):
        self._vuelo.reduciPlazas(self._numPasajeros)
        super().confirmarReserva()

    def cancelarReserva(self):
        self._vuelo.liberarPlazas(self._numPasajeros)
        super().cancelarReserva()

    def getVuelo(self):
        return self.__vuelo