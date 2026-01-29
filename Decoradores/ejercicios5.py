"""Ejercicio 3.3 - Decorador de Logging
Objetivo: Registrar llamadas a funciones (útil para debugging)."""

def decorador_log(func):

    def wrapper(*args, **kwargs):
        print(f"[LOGS] Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args,**kwargs)
        print(f"[LOGS] {func.__name__} retorno: {resultado}")
        return resultado

    return wrapper

@decorador_log
def dividir(a, b):
    return a / b

@decorador_log
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"