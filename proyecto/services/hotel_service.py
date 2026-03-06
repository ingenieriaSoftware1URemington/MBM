# Importa la clase Hotel para crear objetos
from models.hotel import Hotel
# Importa el repositorio que gestiona el almacenamiento de hoteles
from repositories.hotel_repository import HotelRepository

#Aquí están las reglas. Por ejemplo, no puedo crear 
# una reserva si el vuelo no tiene asientos disponibles.


# Clase que contiene la lógica de negocio relacionada con los hoteles
class HotelService:

    # Constructor: recibe el repositorio como dependencia
    def __init__(self, repo: HotelRepository):
        self.__repo = repo

    # Crea un nuevo hotel y lo guarda en el repositorio
    def registrar_hotel(self, id_hotel: int, nombre: str, ciudad: str,
                        categoria: int, plazas_totales: int,
                        plazas_disponibles: int) -> Hotel:
        hotel = Hotel(id_hotel, nombre, ciudad, categoria, plazas_totales, plazas_disponibles)
        self.__repo.guardar(hotel)
        return hotel

    # Busca y retorna un hotel por su id
    def obtener_hotel(self, id_hotel: int) -> Hotel:
        return self.__repo.buscar_por_id(id_hotel)

    # Retorna la lista completa de hoteles registrados
    def listar_hoteles(self) -> list:
        return self.__repo.listar_todos()

    # Elimina un hotel por su id
    def eliminar_hotel(self, id_hotel: int):
        self.__repo.eliminar(id_hotel)