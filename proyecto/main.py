"""
from models.turista import Turista
from repositories.turista_repository import TuristaRepository
from services.turista_service import TuristaService

repo = TuristaRepository()
service = TuristaService(repo)

# Registrar
service.registrar_turista(1, "Ana", "García", "12345678", "ana@mail.com", "3001234567")
service.registrar_turista(2, "Carlos", "López", "87654321", "carlos@mail.com", "3007654321")

# Listar
for turista in service.listar_turistas():
    print(turista)

# Eliminar
service.eliminar_turista(1)
print("Turista 1 eliminado")

# Listar de nuevo
for turista in service.listar_turistas():
    print(turista)

    print("EXITOO")

    """

# ============================================================
# Archivo principal de pruebas del sistema de reservas
# Cubre los 4 casos de prueba requeridos:
#   1. Reserva exitosa
#   2. Reserva sin disponibilidad
#   3. Cancelación de reserva
#   4. Asociación correcta a sucursal
# ============================================================

from models.turista import Turista
from models.vuelo import Vuelo
from models.sucursal import Sucursal

from repositories.turista_repository import TuristaRepository
from repositories.vuelo_repository import VueloRepository
from repositories.sucursal_repository import SucursalRepository
from repositories.reserva_vuelo_repository import ReservaVueloRepository

from services.turista_service import TuristaService
from services.vuelo_service import VueloService
from services.sucursal_service import SucursalService
from services.reserva_vuelo_service import ReservaVueloService

# ── Inicializar repositorios y servicios ──────────────────────
turista_repo    = TuristaRepository()
vuelo_repo      = VueloRepository()
sucursal_repo   = SucursalRepository()
reserva_repo    = ReservaVueloRepository()

turista_service  = TuristaService(turista_repo)
vuelo_service    = VueloService(vuelo_repo)
sucursal_service = SucursalService(sucursal_repo)
reserva_service  = ReservaVueloService(reserva_repo)

# ── Datos base ────────────────────────────────────────────────
# Registrar un turista
turista = turista_service.registrar_turista(
    1, "Ana", "García", "12345678", "ana@mail.com", "3001234567")

# Registrar una sucursal
sucursal = sucursal_service.registrar_sucursal(
    1, "Sucursal Centro", "Bogotá", "Calle 10 # 5-20")

# Registrar un vuelo con 1 plaza disponible
vuelo = vuelo_service.registrar_vuelo(
    1, "AV101", "Bogotá", "Medellín", "2026-03-01", 10, 1)

print("=" * 55)
print("         SISTEMA DE RESERVAS - PRUEBAS BÁSICAS")
print("=" * 55)

# ──────────────────────────────────────────────────────────────
# CASO 1: Reserva exitosa
# Entrada:    vuelo con 1 plaza disponible, turista y sucursal válidos
# Proceso:    crear_reserva valida disponibilidad y confirma
# Resultado esperado: reserva creada con estado "confirmada"
# ──────────────────────────────────────────────────────────────
print("\n[CASO 1] Reserva exitosa")
reserva = reserva_service.crear_reserva(
    1, "2026-02-26", turista, sucursal, 350000.0,
    vuelo, 1, "5A", "economica")
print("Resultado obtenido:", reserva)

# ──────────────────────────────────────────────────────────────
# CASO 2: Reserva sin disponibilidad
# Entrada:    el mismo vuelo que ya quedó sin plazas
# Proceso:    crear_reserva detecta que no hay plazas y lanza excepción
# Resultado esperado: error "No hay plazas disponibles en el vuelo"
# ──────────────────────────────────────────────────────────────
print("\n[CASO 2] Reserva sin disponibilidad")
try:
    reserva_service.crear_reserva(
        2, "2026-02-26", turista, sucursal, 350000.0,
        vuelo, 1, "5B", "economica")
except Exception as e:
    print("Resultado obtenido:", e)

# ──────────────────────────────────────────────────────────────
# CASO 3: Cancelación de reserva
# Entrada:    id de la reserva creada en el caso 1
# Proceso:    cancelar_reserva libera plazas y cambia estado a "cancelada"
# Resultado esperado: estado "cancelada" y plazas del vuelo aumentan en 1
# ──────────────────────────────────────────────────────────────
print("\n[CASO 3] Cancelación de reserva")
reserva_service.cancelar_reserva(1)
reserva_cancelada = reserva_service.obtener_reserva(1)
print("Resultado obtenido:", reserva_cancelada)
print("Plazas vuelo tras cancelar:", vuelo.get_plazas_disponibles())

# ──────────────────────────────────────────────────────────────
# CASO 4: Asociación correcta a sucursal
# Entrada:    sucursal registrada, reserva creada en caso 1
# Proceso:    crear_reserva llama sucursal.agregar_reserva()
# Resultado esperado: la sucursal tiene 1 reserva asociada
# ──────────────────────────────────────────────────────────────
print("\n[CASO 4] Asociación correcta a sucursal")
print("Reservas en sucursal:", len(sucursal.get_reservas()))
for r in sucursal.get_reservas():
    print("Resultado obtenido:", r)

print("\n" + "=" * 55)
print("              PRUEBAS FINALIZADAS")
print("=" * 55)