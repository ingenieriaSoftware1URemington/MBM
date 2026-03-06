# Importa la clase Vuelo para crear objetos
from models.vuelo import Vuelo
# Importa el repositorio que gestiona el almacenamiento de vuelos
from repositories.vuelo_repository import VueloRepository

# Clase que contiene la lógica de negocio relacionada con los vuelos
class VueloService:

    # Constructor: recibe el repositorio como dependencia
    def __init__(self, repo: VueloRepository):
        self.__repo = repo

    # Crea un nuevo vuelo y lo guarda en el repositorio
    def registrar_vuelo(self, id_vuelo: int, numero_vuelo: str, origen: str,
                        destino: str, fecha_salida: str, plazas_total: int,
                        plazas_disponibles: int) -> Vuelo:
        vuelo = Vuelo(id_vuelo, numero_vuelo, origen, destino, fecha_salida,
                      plazas_total, plazas_disponibles)
        self.__repo.guardar(vuelo)
        return vuelo

    # Busca y retorna un vuelo por su id
    def obtener_vuelo(self, id_vuelo: int) -> Vuelo:
        return self.__repo.buscar_por_id(id_vuelo)

    # Retorna la lista completa de vuelos registrados
    def listar_vuelos(self) -> list:
        return self.__repo.listar_todos()

    # Elimina un vuelo por su id
    def eliminar_vuelo(self, id_vuelo: int):
        self.__repo.eliminar(id_vuelo)