# Definición de la clase Turista que representa a un turista en el sistema
class Turista:

    # Constructor: se ejecuta automáticamente al crear un objeto Turista
    # Recibe los datos del turista con sus tipos definidos
    def __init__(self, id_turista: int, nombre: str, apellido: str, documento: str,
                 email: str, telefono: str):
        
        # Atributo privado (doble guión) que almacena el id único del turista
        self.__id_turista = id_turista
        # Atributo privado que almacena el nombre del turista
        self.__nombre = nombre
        # Atributo privado que almacena el apellido del turista
        self.__apellido = apellido
        # Atributo privado que almacena el número de documento del turista
        self.__documento = documento
        # Atributo privado que almacena el email del turista
        self.__email = email
        # Atributo privado que almacena el teléfono del turista
        self.__telefono = telefono

    # Getter: retorna el id del turista
    def get_id(self):
        return self.__id_turista

    # Getter: retorna el nombre del turista
    def get_nombre(self):
        return self.__nombre

    # Getter: retorna el apellido del turista
    def get_apellido(self):
        return self.__apellido

    # Getter: retorna el documento del turista
    def get_documento(self):
        return self.__documento

    # Getter: retorna el email del turista
    def get_email(self):
        return self.__email

    # Getter: retorna el teléfono del turista
    def get_telefono(self):
        return self.__telefono

    # Setter: permite actualizar el email del turista
    def set_email(self, nuevo_email: str):
        self.__email = nuevo_email

    # Setter: permite actualizar el teléfono del turista
    def set_telefono(self, nuevo_telefono: str):
        self.__telefono = nuevo_telefono

    # Método que imprime en consola la información del turista
    # Llama internamente al método __str__
    def mostrar_info(self):
        print(self.__str__())

    # Método especial de Python que define cómo se representa el objeto como texto
    # Se ejecuta automáticamente al hacer print(turista)
    def __str__(self):
        return (f"Turista [{self.__id_turista}] "   # muestra el id entre corchetes
            f"{self.__nombre} {self.__apellido} " # nombre y apellido juntos
            f"| Doc: {self.__documento} "         # el documento
            f"| Email: {self.__email} "           # el email
            f"| Tel: {self.__telefono}")           # el telefono