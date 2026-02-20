from collections import deque

def ejecutar_procesos(procesos: list[tuple]) -> None:
    cola = deque()
    cola.extend(procesos)
    while cola:
        proceso = cola.popleft()
        proceso_segundo = proceso[1]
        segundo_restado = proceso_segundo - 1
        if segundo_restado != 0:
            proceso_restado = (proceso[0],segundo_restado)
            print(f"Procesando {proceso[0]}... le faltan {segundo_restado}")
            cola.append(proceso_restado)
        else:
            print(f"{proceso[0]} ha terminado")
ejecutar_procesos([("Nginx", 3), ("Postgres", 1), ("Redis", 2)])