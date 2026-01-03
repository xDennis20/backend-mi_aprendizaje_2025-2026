
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
for s in lista_logs:
    separador_fecha = s.split("]")
    parte_importante = separador_fecha[1].split(":")
    if "INFO" in parte_importante[0]:
        estados["INFO"] +=1
    elif "WARN" in parte_importante[0]:
        estados["WARN"] +=1
    elif "ERROR" in parte_importante[0]:
        estados["ERROR"] +=1
print(estados)