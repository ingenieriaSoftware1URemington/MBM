# DOCUMENTACION
## SISTEMA DE RESERVA, AGENCIA DE VIAJES


### Descripción General del Proyecto

Este proyecto implementa un sistema de gestión de reservas para una agencia de viajes, utilizando el patrón de arquitectura MVC (Modelo-Vista-Controlador) en Python. El sistema permite registrar turistas, vuelos, hoteles y sucursales, así como crear y gestionar reservas de vuelo.


### Archivos del Proyecto
- turista.py	Modelo Turista con atributos privados, getters, setters y _str_

- vuelo.py	Modelo Vuelo con control de plazas disponibles

- hotel.py	Modelo Hotel con control de plazas y disponibilidad

- sucursal.py	Modelo Sucursal con lista interna de reservas

- reserva_vuelo.py	Modelo ReservaVuelo que asocia turista, vuelo y sucursal

- turista_repository.py	Almacenamiento de turistas; búsqueda por id y por documento

- vuelo_repository.py	Almacenamiento de vuelos en diccionario

- hotel_repository.py	Almacenamiento de hoteles en diccionario

- sucursal_repository.py	Almacenamiento de sucursales en diccionario

- reserva_vuelo_repository.py	Almacenamiento de reservas de vuelo

- turista_service.py	Lógica de negocio para turistas

- vuelo_service.py	Lógica de negocio para vuelos

- hotel_service.py	Lógica de negocio para hoteles

- sucursal_service.py	Lógica de negocio para sucursales

- reserva_vuelo_service.py	Lógica de negocio para reservas: validación, confirmación y cancelación


## 1. REGISTRAR TURISTA

1. Entrada
* id_turista: 1
* nombre: "Carlos"
* apellido: "Gomez"
* documento: "123456789"
* email: "carlos@email.com"
* telefono: "3001234567"

2. Proceso
1.	TuristaService.registrar_turista() crea un objeto Turista con los datos recibidos.
2.	Llama a TuristaRepository.guardar(turista) para almacenarlo en el diccionario interno.
3.	La clave del diccionario es el id_turista del objeto.

3. Resultado Esperado
El turista queda almacenado en memoria. Al llamar listar_turistas() aparece en la lista.

4. Resultado Obtenido
repo = TuristaRepository()
service = TuristaService(repo)
t = service.registrar_turista(1, 'Carlos', 'Gomez', '123456789', 'carlos@email.com', '3001234567')
print(t)
Salida: Turista [1] Carlos Gomez | Doc: 123456789 | Email: carlos@email.com | Tel: 3001234567

## 2. CREAR RESERVA


1. Entrada
* id_reserva: 1
* fecha_reserva: "2025-05-01"
* turista: objeto Turista registrado
* sucursal: objeto Sucursal registrada
* monto: 350000.0
* vuelo: objeto Vuelo con plazas disponibles > 0
* num_pasajeros: 1
* asientos: "12A"
* clase: "economica"

2. Proceso
10.	ReservaVueloService.crear_reserva() verifica que vuelo.consultar_disponibilidad() sea True.
11.	Crea un objeto ReservaVuelo en estado 'pendiente'.
12.	Llama a reserva.confirmar_reserva() que reduce una plaza del vuelo y cambia estado a 'confirmada'.
13.	Asocia la reserva a la sucursal con sucursal.agregar_reserva(reserva).
14.	Guarda la reserva en el repositorio.

3. Resultado Esperado
La reserva se crea y confirma. El vuelo pasa de 100 a 99 plazas disponibles.

4. Resultado Obtenido
reserva = service_r.crear_reserva(1, '2025-05-01', turista, sucursal,350000.0, vuelo, 1, '12A', 'economica')

print(reserva)
Salida: Reserva [1] | Estado: confirmada | Turista: Carlos | Vuelo: AV101 | Pasajeros: 1 | Clase: economica | Monto: $350000.0

## 3. RESERVA SIN DISPONIBILIDAD

1. Entrada
* vuelo con plazas_disponibles: 0
* Demás datos de reserva iguales al caso anterior

2. Proceso
15.	ReservaVueloService.crear_reserva() llama a vuelo.consultar_disponibilidad().
16.	El método retorna False porque plazas_disponibles == 0.
17.	El servicio lanza una excepcion: raise Exception('No hay plazas disponibles en el vuelo').
18.	No se crea ni guarda ninguna reserva.

3. Resultado Esperado
El sistema lanza una excepcion controlada e impide crear la reserva.

4. Resultado Obtenido
### Vuelo sin plazas
vuelo_lleno = Vuelo(2, 'AV202', 'Cali', 'Bogota', '2025-07-01', 50, 0)
try:
    service_r.crear_reserva(2, '2025-05-01', turista, sucursal, 200000, vuelo_lleno, 1, '5B', 'economica')
except Exception as e:
    print(e)  # No hay plazas disponibles en el vuelo
Salida: Exception: No hay plazas disponibles en el vuelo

## 4. CANCELAR RESERVA

1. Entrada
* id_reserva: 1
* (La reserva debe existir en el repositorio y estar en estado 'confirmada')

2. Proceso
19.	ReservaVueloService.cancelar_reserva() busca la reserva en el repositorio por su id.
20.	Si no existe, lanza una excepcion: 'Reserva no encontrada'.
21.	Si existe, llama a reserva.cancelar_reserva() que libera una plaza del vuelo.
22.	El estado de la reserva cambia a 'cancelada'.

3. Resultado Esperado
La reserva pasa a estado 'cancelada' y el vuelo recupera una plaza disponible.

4. Resultado Obtenido
service_r.cancelar_reserva(1)
reserva = service_r.obtener_reserva(1)
print(reserva.get_estado())  # cancelada
print(vuelo.get_plazas_disponibles())  # 100
Salida: Estado de reserva: cancelada. Vuelo vuelve a tener 100 plazas disponibles.

