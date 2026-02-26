class Vuelo:

#constructor
    def __init__(self, id_vuelo: int, numero_vuelo: str, origen: str,
                 destino: str, fecha_salida: str, plazas_total: int, plazas_disponibles: int):
        
        self.__id_vuelo = id_vuelo
        self.__numero_vuelo = numero_vuelo
        self.__origen = origen
        self.__destino = destino
        self.__decha_salida = fecha_salida
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

    def librerar_plazas(self):
        if self.__plazas_disponibles < self.__plazas_total:
            self.__plazas_disponibles += 1

    #def numero_vuelo(self) -> str:
        #return self.__numero_vuelo





