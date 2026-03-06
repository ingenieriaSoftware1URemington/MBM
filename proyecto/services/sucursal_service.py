# Importa la clase Sucursal para crear objetos
from models.sucursal import Sucursal
# Importa el repositorio que gestiona el almacenamiento de sucursales
from repositories.sucursal_repository import SucursalRepository

# Clase que contiene la lógica de negocio relacionada con las sucursales
class SucursalService:

    # Constructor: recibe el repositorio como dependencia
    def __init__(self, repo: SucursalRepository):
        self.__repo = repo

    # Crea una nueva sucursal y la guarda en el repositorio
    def registrar_sucursal(self, id_sucursal: int, nombre: str,
                           ciudad: str, direccion: str) -> Sucursal:
        sucursal = Sucursal(id_sucursal, nombre, ciudad, direccion)
        self.__repo.guardar(sucursal)
        return sucursal

    # Busca y retorna una sucursal por su id
    def obtener_sucursal(self, id_sucursal: int) -> Sucursal:
        return self.__repo.buscar_por_id(id_sucursal)

    # Retorna la lista completa de sucursales registradas
    def listar_sucursales(self) -> list:
        return self.__repo.listar_todos()

    # Elimina una sucursal por su id
    def eliminar_sucursal(self, id_sucursal: int):
        self.__repo.eliminar(id_sucursal)