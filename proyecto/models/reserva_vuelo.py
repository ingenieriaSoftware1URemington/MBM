"""
from models.vuelo import Vuelo
from models.reserva import Reserva

class ReservaVuelo(Reserva):

    def __init__(self, idReserva, fechaReserva, estado, turista, sucursal, monto,
                 vuelo: Vuelo, numPasajeros: int, asientos: str, clase: str):
        super().__init__(idReserva, fechaReserva, estado, turista, sucursal, monto)
        self.__vuelo = vuelo
        self.__numPasajeros = numPasajeros
        self.__asientos = asientos
        self.__clase = clase

    def validar_disponibilidad(self):
        return self.__vuelo.consultar_disponibilidad()

    def confirmar_reserva(self):
        self.__vuelo.reducir_plazas()
        super().confirmar_reserva()

    def cancelar_reserva(self):
        self.__vuelo.liberar_plazas()
        super().cancelar_reserva()

    def get_vuelo(self):
        return self.__vuelo
        """
# Importa Vuelo para asociarlo a la reserva
from models.vuelo import Vuelo
# Importa Turista para asociarlo a la reserva
from models.turista import Turista
# Importa Sucursal para asociarla a la reserva
from models.sucursal import Sucursal

# Clase que representa una reserva de vuelo en el sistema
# No hereda de Reserva ya que no existe esa clase base definida
class ReservaVuelo:

    # Constructor: inicializa la reserva con todos sus datos
    def __init__(self, id_reserva: int, fecha_reserva: str, estado: str,
                 turista: Turista, sucursal: Sucursal, monto: float,
                 vuelo: Vuelo, num_pasajeros: int, asientos: str, clase: str):

        # Id único de la reserva
        self.__id_reserva = id_reserva
        # Fecha en que se realizó la reserva
        self.__fecha_reserva = fecha_reserva
        # Estado de la reserva: "pendiente", "confirmada", "cancelada"
        self.__estado = estado
        # Turista que realizó la reserva
        self.__turista = turista
        # Sucursal desde donde se hizo la reserva
        self.__sucursal = sucursal
        # Monto total de la reserva
        self.__monto = monto
        # Vuelo asociado a la reserva
        self.__vuelo = vuelo
        # Número de pasajeros incluidos en la reserva
        self.__num_pasajeros = num_pasajeros
        # Asientos asignados
        self.__asientos = asientos
        # Clase del vuelo: "economica", "business", etc.
        self.__clase = clase

    # Getter: retorna el id de la reserva
    def get_id(self):
        return self.__id_reserva

    # Getter: retorna el estado de la reserva
    def get_estado(self):
        return self.__estado

    # Getter: retorna el vuelo asociado
    def get_vuelo(self):
        return self.__vuelo

    # Getter: retorna el turista asociado
    def get_turista(self):
        return self.__turista

    # Verifica si el vuelo tiene plazas disponibles
    def validar_disponibilidad(self):
        return self.__vuelo.consultar_disponibilidad()

    # Confirma la reserva: reduce las plazas del vuelo y cambia el estado
    def confirmar_reserva(self):
        self.__vuelo.reducir_plazas()
        self.__estado = "confirmada"

    # Cancela la reserva: libera las plazas del vuelo y cambia el estado
    def cancelar_reserva(self):
        self.__vuelo.liberar_plazas()
        self.__estado = "cancelada"

    # Representa el objeto como texto al hacer print(reserva)
    def __str__(self):
        return (f"Reserva [{self.__id_reserva}] "
                f"| Estado: {self.__estado} "
                f"| Turista: {self.__turista.get_nombre()} "
                f"| Vuelo: {self.__vuelo.get_numero_vuelo()} "
                f"| Pasajeros: {self.__num_pasajeros} "
                f"| Clase: {self.__clase} "
                f"| Monto: ${self.__monto}")
