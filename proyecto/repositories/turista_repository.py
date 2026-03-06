# Importa la clase Turista para usarla como tipo de dato en los métodos
from models.turista import Turista

# Clase que gestiona el almacenamiento de objetos Turista en memoria
class TuristaRepository:

    # Constructor: inicializa el diccionario vacío donde se guardarán los turistas
    def __init__(self):
        # Diccionario privado con estructura { id_turista: objeto Turista }
        self.__turistas = {}

    # Guarda un objeto Turista en el diccionario usando su id como clave
    # _Turista__id_turista es la forma de acceder a un atributo privado desde fuera de la clase
    def guardar(self, turista: Turista):
        self.__turistas[turista._Turista__id_turista] = turista

    # Busca y retorna un turista por su id
    # Si no existe, retorna None gracias al segundo parámetro del método get
    def buscar_por_id(self, id_turista: int) -> Turista:
        return self.__turistas.get(id_turista, None)
    
    # Busca un turista recorriendo todos los registros hasta encontrar el documento
    # Si no lo encuentra, retorna None
    def buscar_por_documento(self, documento: str) -> Turista:
        for turista in self.__turistas.values():
            # Accede al atributo privado __documento desde fuera de la clase
            if turista._Turista__documento == documento:
                return turista
        return None

    # Retorna todos los turistas almacenados como una lista
    def listar_todos(self) -> list:
        return list(self.__turistas.values())
    
    # Elimina un turista del diccionario si existe
    def eliminar(self, id_turista: int):
        # Verifica que el id exista antes de intentar eliminar
        if id_turista in self.__turistas:
            del self.__turistas[id_turista]