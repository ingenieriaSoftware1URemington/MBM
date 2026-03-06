# Importa la clase ReservaVuelo para crear objetos
from models.reserva_vuelo import ReservaVuelo
# Importa el repositorio de reservas
from repositories.reserva_vuelo_repository import ReservaVueloRepository

# Clase que contiene la lógica de negocio relacionada con las reservas de vuelo
class ReservaVueloService:

    # Constructor: recibe el repositorio como dependencia
    def __init__(self, repo: ReservaVueloRepository):
        self.__repo = repo

    # Crea una nueva reserva si el vuelo tiene disponibilidad
    def crear_reserva(self, id_reserva, fecha_reserva, turista,
                      sucursal, monto, vuelo, num_pasajeros,
                      asientos, clase) -> ReservaVuelo:

        # Caso de prueba: Reserva sin disponibilidad
        # Si el vuelo no tiene plazas, lanza un error y no crea la reserva
        if not vuelo.consultar_disponibilidad():
            raise Exception("No hay plazas disponibles en el vuelo")

        # Crea el objeto reserva en estado "pendiente"
        reserva = ReservaVuelo(id_reserva, fecha_reserva, "pendiente",
                               turista, sucursal, monto, vuelo,
                               num_pasajeros, asientos, clase)

        # Caso de prueba: Reserva exitosa
        # Confirma la reserva: reduce plazas y cambia estado a "confirmada"
        reserva.confirmar_reserva()

        # Asocia la reserva a la sucursal correspondiente
        # Caso de prueba: Asociación correcta a sucursal
        sucursal.agregar_reserva(reserva)

        # Guarda la reserva en el repositorio
        self.__repo.guardar(reserva)
        return reserva

    # Busca y retorna una reserva por su id
    def obtener_reserva(self, id_reserva: int) -> ReservaVuelo:
        return self.__repo.buscar_por_id(id_reserva)

    # Cancela una reserva existente: libera plazas y cambia estado a "cancelada"
    # Caso de prueba: Cancelación de reserva
    def cancelar_reserva(self, id_reserva: int):
        reserva = self.__repo.buscar_por_id(id_reserva)
        if not reserva:
            raise Exception("Reserva no encontrada")
        # Libera las plazas del vuelo y cambia el estado
        reserva.cancelar_reserva()

    # Retorna la lista completa de reservas registradas
    def listar_reservas(self) -> list:
        return self.__repo.listar_todos()