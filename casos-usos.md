#Casos de Uso

Aquí tienes el contenido organizado con una estructura de Markdown clara, profesional y fácil de leer:

---

## RF-01: Procesamiento de Transacciones de Pago

El sistema debe permitir a los comercios **procesar pagos digitales** de sus clientes en tiempo real.

* **Métodos soportados:** Debe admitir múltiples formas de pago (tarjetas de débito/crédito, transferencias y billeteras digitales).
* **Comprobantes:** Generación automática de recibos para cada transacción exitosa.
* **Registro de datos:** Cada transacción debe incluir:
* *Timestamp* (marca de tiempo).
* Monto.
* Comercio.
* Usuario.
* Estado.



---

## RF-02: Validar archivos bancarios

El sistema debe realizar una **conciliación automática** comparando las transacciones de la plataforma con los registros del banco para identificar:

* Faltantes y duplicados.
* Diferencias en montos.
* Problemas de estado.

---

## RF-03: Gestión de Usuarios y Roles

Implementación de un sistema de control de acceso y seguridad:

* **Autenticación:** Acceso seguro para empleados, comercios y usuarios finales.
* **Roles y Permisos:** Definición de niveles (Administrador, Operador, Comercio, Usuario).
* **Auditoría:** Registro de *logs* de todas las acciones realizadas por los usuarios.
* **Recuperación:** Proceso de restablecimiento de contraseñas mediante verificación segura.

---

## RF-04: Notificaciones y Comunicaciones

Gestión de alertas y avisos del sistema:

* **Estado de Transacciones:** Envío de notificaciones vía Email/SMS a usuarios y comercios.
* **Alertas Críticas:** Aviso a administradores sobre fallos del sistema, transacciones rechazadas o actividades sospechosas.
* **Personalización:** Configuración de preferencias de notificación según el perfil del usuario o comercio.

---


![casos de uso](IMG/TAREA1.png)
![casos de uso](IMG/TAREA2.png)
![casos de uso](IMG/TAREA3.png)
![casos de uso](IMG/TAREA4.png)


