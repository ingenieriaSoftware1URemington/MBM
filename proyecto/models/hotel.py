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
        if self.__plazas_disponibles < self.__plazas_total:
            self.__plazas_disponibles += 1