"""
class Hotel:

    def __init__(self, id_hotel: int, nombre: str, ciudad: str, categoria: int,
             plazas_totales: int, plazas_disponibles: int):
    
        self.__id_hotel = id_hotel
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__categoria = categoria
        self.__plazas_totales = plazas_totales
        self.__plazas_disponibles = plazas_disponibles

    def registrar_hotel(self):
        pass

    def consultar_disponibilidad(self):
        return self.__plazas_disponibles > 0
    
    def reducir_plazas(self):
        if self.__plazas_disponibles > 0:
            self.__plazas_disponibles -=1

    def liberar_plazas(self):
        if self.__plazas_disponibles < self.__plazas_totales:
            self.__plazas_disponibles += 1
            """

#Aquí están los datos. Un turista tiene nombre, documento y 
# email. Un vuelo tiene origen, destino y asientos.

# Clase que representa un hotel disponible en el sistema
class Hotel:

    # Constructor: inicializa el hotel con todos sus datos
    def __init__(self, id_hotel: int, nombre: str, ciudad: str, categoria: int,
                 plazas_totales: int, plazas_disponibles: int):

        # Id único del hotel
        self.__id_hotel = id_hotel
        # Nombre del hotel
        self.__nombre = nombre
        # Ciudad donde está ubicado
        self.__ciudad = ciudad
        # Categoría en estrellas (1 a 5)
        self.__categoria = categoria
        # Total de plazas del hotel
        self.__plazas_totales = plazas_totales
        # Plazas actualmente disponibles
        self.__plazas_disponibles = plazas_disponibles

    #GETTER leer datos
    #SETTER modificar datos

    # Getter: retorna el id del hotel
    def get_id(self):
        return self.__id_hotel

    # Getter: retorna el nombre del hotel
    def get_nombre(self):
        return self.__nombre

    # Getter: retorna la ciudad del hotel
    def get_ciudad(self):
        return self.__ciudad

    # Getter: retorna las plazas disponibles
    def get_plazas_disponibles(self):
        return self.__plazas_disponibles

    # Retorna True si hay al menos una plaza disponible
    def consultar_disponibilidad(self):
        return self.__plazas_disponibles > 0

    # Reduce en 1 las plazas disponibles si hay alguna
    def reducir_plazas(self):
        if self.__plazas_disponibles > 0:
            self.__plazas_disponibles -= 1

    # Aumenta en 1 las plazas disponibles si no se superan las totales
    def liberar_plazas(self):
        if self.__plazas_disponibles < self.__plazas_totales:
            self.__plazas_disponibles += 1

    # Representa el objeto como texto al hacer print(hotel)
    def __str__(self):
        return (f"Hotel [{self.__id_hotel}] {self.__nombre} "
                f"| Ciudad: {self.__ciudad} "
                f"| Categoría: {self.__categoria}★ "
                f"| Plazas disponibles: {self.__plazas_disponibles}/{self.__plazas_totales}")