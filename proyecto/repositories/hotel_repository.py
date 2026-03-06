# Importa la clase Hotel para usarla como tipo de dato
from models.hotel import Hotel

#Es como una lista en memoria. Puedo guardar un turista,
# buscarlo por id, o eliminar

# Clase que gestiona el almacenamiento de objetos Hotel en memoria
class HotelRepository:

    # Constructor: inicializa el diccionario vacío de hoteles
    def __init__(self):
        # Diccionario privado con estructura { id_hotel: objeto Hotel }
        self.__hoteles = {}

    # Guarda un hotel en el diccionario usando su id como clave
    def guardar(self, hotel: Hotel):
        self.__hoteles[hotel._Hotel__id_hotel] = hotel

    # Busca y retorna un hotel por su id, o None si no existe
    def buscar_por_id(self, id_hotel: int) -> Hotel:
        return self.__hoteles.get(id_hotel, None)

    # Retorna todos los hoteles almacenados como lista
    def listar_todos(self) -> list:
        return list(self.__hoteles.values())

    # Elimina un hotel del diccionario si existe
    def eliminar(self, id_hotel: int):
        if id_hotel in self.__hoteles:
            del self.__hoteles[id_hotel]