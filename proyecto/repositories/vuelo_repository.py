# Importa la clase Vuelo para usarla como tipo de dato
from models.vuelo import Vuelo

# Clase que gestiona el almacenamiento de objetos Vuelo en memoria
class VueloRepository:

    # Constructor: inicializa el diccionario vacío de vuelos
    def __init__(self):
        # Diccionario privado con estructura { id_vuelo: objeto Vuelo }
        self.__vuelos = {}

    # Guarda un vuelo en el diccionario usando su id como clave
    def guardar(self, vuelo: Vuelo):
        self.__vuelos[vuelo._Vuelo__id_vuelo] = vuelo

    # Busca y retorna un vuelo por su id, o None si no existe
    def buscar_por_id(self, id_vuelo: int) -> Vuelo:
        return self.__vuelos.get(id_vuelo, None)

    # Retorna todos los vuelos almacenados como lista
    def listar_todos(self) -> list:
        return list(self.__vuelos.values())

    # Elimina un vuelo del diccionario si existe
    def eliminar(self, id_vuelo: int):
        if id_vuelo in self.__vuelos:
            del self.__vuelos[id_vuelo]