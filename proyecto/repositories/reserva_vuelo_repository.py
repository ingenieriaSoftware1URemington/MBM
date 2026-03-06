# Importa la clase ReservaVuelo para usarla como tipo de dato
from models.reserva_vuelo import ReservaVuelo

# Clase que gestiona el almacenamiento de objetos ReservaVuelo en memoria
class ReservaVueloRepository:

    # Constructor: inicializa el diccionario vacío de reservas
    def __init__(self):
        # Diccionario privado con estructura { id_reserva: objeto ReservaVuelo }
        self.__reservas = {}

    # Guarda una reserva en el diccionario usando su id como clave
    def guardar(self, reserva: ReservaVuelo):
        self.__reservas[reserva._ReservaVuelo__id_reserva] = reserva

    # Busca y retorna una reserva por su id, o None si no existe
    def buscar_por_id(self, id_reserva: int) -> ReservaVuelo:
        return self.__reservas.get(id_reserva, None)

    # Retorna todas las reservas almacenadas como lista
    def listar_todos(self) -> list:
        return list(self.__reservas.values())

    # Elimina una reserva del diccionario si existe
    def eliminar(self, id_reserva: int):
        if id_reserva in self.__reservas:
            del self.__reservas[id_reserva]