def wraper_nueva_funcion(funcion_original,nombre):
    def wrapper(*args,**kwargs):
        print(f"Ejecutando {nombre}")
        return funcion_original(*args,**kwargs)
    return wrapper

def log_todo(cls):
    nombres = dir(cls)
    for nombre in nombres:
        if nombre.startswith("__"):
            continue
        funcion_real = getattr(cls, nombre)
        if not callable(funcion_real):
            continue
        nueva_funcion = wraper_nueva_funcion(funcion_real,nombre)
        setattr(cls,nombre,nueva_funcion)
    return cls

@log_todo
class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        return f"Depositados {monto}. Saldo: {self.saldo}"

    def retirar(self, monto):
        self.saldo -= monto
        return f"Retirados {monto}. Saldo: {self.saldo}"