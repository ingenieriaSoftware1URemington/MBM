# Importa la clase Turista para usarla como tipo de dato
from models.turista import Turista
# Importa el repositorio que gestiona el almacenamiento de turistas
from repositories.turista_repository import TuristaRepository

# Clase que contiene la lógica de negocio relacionada con los turistas
# Se comunica con el repositorio para guardar y recuperar datos
class TuristaService:

    # Constructor: recibe el repositorio como dependencia (inyección de dependencias)
    # Esto permite que el servicio no dependa de cómo se almacenan los datos
    def __init__(self, repo: TuristaRepository):
        self.__repo = repo

    # Crea un nuevo objeto Turista y lo guarda en el repositorio
    # Retorna el turista creado
    def registrar_turista(self, id_turista: int, nombre: str, apellido: str,
                          documento: str, email: str, telefono: str) -> Turista:
        # Crea el objeto Turista con los datos recibidos
        turista = Turista(id_turista, nombre, apellido, documento, email, telefono)
        # Le pide al repositorio que lo guarde
        self.__repo.guardar(turista)
        # Retorna el turista creado
        return turista

    # Busca y retorna un turista por su id
    # Si no existe, el repositorio retorna None
    def obtener_turista(self, id_turista: int) -> Turista:
        return self.__repo.buscar_por_id(id_turista)

    # Retorna la lista completa de turistas almacenados
    def listar_turistas(self) -> list:
        return self.__repo.listar_todos()

    # Elimina un turista del repositorio por su id
    def eliminar_turista(self, id_turista: int):
        self.__repo.eliminar(id_turista)