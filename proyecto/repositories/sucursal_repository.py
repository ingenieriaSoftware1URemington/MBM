# Importa la clase Sucursal para usarla como tipo de dato
from models.sucursal import Sucursal

# Clase que gestiona el almacenamiento de objetos Sucursal en memoria
class SucursalRepository:

    # Constructor: inicializa el diccionario vacío de sucursales
    def __init__(self):
        # Diccionario privado con estructura { id_sucursal: objeto Sucursal }
        self.__sucursales = {}

    # Guarda una sucursal en el diccionario usando su id como clave
    def guardar(self, sucursal: Sucursal):
        self.__sucursales[sucursal._Sucursal__id_sucursal] = sucursal

    # Busca y retorna una sucursal por su id, o None si no existe
    def buscar_por_id(self, id_sucursal: int) -> Sucursal:
        return self.__sucursales.get(id_sucursal, None)

    # Retorna todas las sucursales almacenadas como lista
    def listar_todos(self) -> list:
        return list(self.__sucursales.values())

    # Elimina una sucursal del diccionario si existe
    def eliminar(self, id_sucursal: int):
        if id_sucursal in self.__sucursales:
            del self.__sucursales[id_sucursal]