"""
class Sucursal:

    def __init__(self, id_turista: int, nombre: str, ciudad: str,
              direccion: str, reservas: list):
    
        self.__id_turista = id_turista
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__reservas = reservas

    def registrar_sucursal(self):
        pass

    def get_nombre(self):
        pass

    def agregar_Reserva(self):
        pass

    def get_reservas(self):
        pass
    
    def mostrar_info(self):
        pass
        """
# Clase que representa una sucursal de la agencia de viajes
class Sucursal:

    # Constructor: inicializa la sucursal con sus datos
    # Se corrige el error original: __init faltaba doble guión al final
    def __init__(self, id_sucursal: int, nombre: str, ciudad: str,
                 direccion: str):

        # Id único de la sucursal
        self.__id_sucursal = id_sucursal
        # Nombre de la sucursal
        self.__nombre = nombre
        # Ciudad donde está ubicada
        self.__ciudad = ciudad
        # Dirección física
        self.__direccion = direccion
        # Lista interna de reservas asociadas a esta sucursal
        self.__reservas = []

    # Getter: retorna el id de la sucursal
    def get_id(self):
        return self.__id_sucursal

    # Getter: retorna el nombre de la sucursal
    def get_nombre(self):
        return self.__nombre

    # Getter: retorna la ciudad de la sucursal
    def get_ciudad(self):
        return self.__ciudad

    # Agrega una reserva a la lista de reservas de la sucursal
    def agregar_reserva(self, reserva):
        self.__reservas.append(reserva)

    # Getter: retorna la lista de reservas de la sucursal
    def get_reservas(self):
        return self.__reservas

    # Representa el objeto como texto al hacer print(sucursal)
    def __str__(self):
        return (f"Sucursal [{self.__id_sucursal}] {self.__nombre} "
                f"| Ciudad: {self.__ciudad} "
                f"| Dirección: {self.__direccion} "
                f"| Reservas: {len(self.__reservas)}")