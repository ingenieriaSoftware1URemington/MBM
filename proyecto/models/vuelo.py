"""
class Vuelo:

#constructor
    def __init__(self, id_vuelo: int, numero_vuelo: str, origen: str,
                 destino: str, fecha_salida: str, plazas_total: int, plazas_disponibles: int):
        
        self.__id_vuelo = id_vuelo
        self.__numero_vuelo = numero_vuelo
        self.__origen = origen
        self.__destino = destino
        self.__fecha_salida = fecha_salida
        self.__plazas_total = plazas_total
        self.__plazas_disponibles = plazas_disponibles


    #metodos    
    def registrar_vuelo(self):
        pass

    def consultar_disponibilidad(self):
        return self.__plazas_disponibles > 0

    def reducir_plazas(self):
        if self.__plazas_disponibles > 0:
            self.__plazas_disponibles -=1

    def liberar_plazas(self):
        if self.__plazas_disponibles < self.__plazas_total:
            self.__plazas_disponibles += 1

    #def numero_vuelo(self) -> str:
        #return self.__numero_vuelo
        """
# Clase que representa un vuelo disponible en el sistema
class Vuelo:

    # Constructor: inicializa el vuelo con todos sus datos
    def __init__(self, id_vuelo: int, numero_vuelo: str, origen: str,
                 destino: str, fecha_salida: str, plazas_total: int, plazas_disponibles: int):

        # Id único del vuelo
        self.__id_vuelo = id_vuelo
        # Código del vuelo (ej: "AV123")
        self.__numero_vuelo = numero_vuelo
        # Ciudad de origen
        self.__origen = origen
        # Ciudad de destino
        self.__destino = destino
        # Fecha de salida del vuelo
        self.__fecha_salida = fecha_salida
        # Total de plazas del vuelo
        self.__plazas_total = plazas_total
        # Plazas actualmente disponibles
        self.__plazas_disponibles = plazas_disponibles

    # Getter: retorna el id del vuelo
    def get_id(self):
        return self.__id_vuelo

    # Getter: retorna el número de vuelo
    def get_numero_vuelo(self):
        return self.__numero_vuelo

    # Getter: retorna el origen del vuelo
    def get_origen(self):
        return self.__origen

    # Getter: retorna el destino del vuelo
    def get_destino(self):
        return self.__destino

    # Getter: retorna la fecha de salida
    def get_fecha_salida(self):
        return self.__fecha_salida

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
        if self.__plazas_disponibles < self.__plazas_total:
            self.__plazas_disponibles += 1

    # Representa el objeto como texto al hacer print(vuelo)
    def __str__(self):
        return (f"Vuelo [{self.__id_vuelo}] {self.__numero_vuelo} "
                f"| {self.__origen} → {self.__destino} "
                f"| Fecha: {self.__fecha_salida} "
                f"| Plazas disponibles: {self.__plazas_disponibles}/{self.__plazas_total}")





