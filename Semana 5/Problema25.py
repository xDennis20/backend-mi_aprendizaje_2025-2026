"""
RETO BACKEND: EL ANALISTA DE LOGS
--------------------------------------------------------------------------------
Objetivo:
    Procesar un volcado de logs (texto crudo) para extraer métricas clave
    sin utilizar librerías externas (solo Python puro).

Métricas a obtener:
    1. Conteo total de eventos por tipo (INFO, WARN, ERROR).
    2. Identificación del mensaje de error más frecuente (El Culpable).

Input: Cadena de texto con fecha, tipo de evento y mensaje.
Output: Diccionario de conteo y string del error más común."""

raw_logs = """
[2026-01-02 14:00:00] INFO: User_123 logged in
[2026-01-02 14:00:05] WARN: High memory usage detected
[2026-01-02 14:01:10] ERROR: Database connection failed
[2026-01-02 14:01:15] INFO: User_456 logged in
[2026-01-02 14:02:00] ERROR: Timeout request at /api/v1/products
[2026-01-02 14:02:30] ERROR: Database connection failed
[2026-01-02 14:03:00] INFO: User_123 logged out
[2026-01-02 14:03:05] ERROR: Database connection failed
"""
logs_limpios = raw_logs.strip()
lista_logs = logs_limpios.splitlines()
estados = {
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0
}
mensajes_error = {}
for s in lista_logs:
    separador_fecha = s.split("]")
    parte_importante = separador_fecha[1].strip().split(":")
    if "INFO" == parte_importante[0]:
        estados["INFO"] +=1
    elif "WARN" == parte_importante[0]:
        estados["WARN"] +=1
    elif "ERROR" == parte_importante[0]:
        estados["ERROR"] +=1
    mensaje = parte_importante[1].strip()
    if mensaje in mensajes_error:
        mensajes_error[mensaje] +=1
    else:
        mensajes_error[mensaje] = 1
print(f"Conteo: "
      f"{estados}")
print(max(mensajes_error, key=mensajes_error.get))