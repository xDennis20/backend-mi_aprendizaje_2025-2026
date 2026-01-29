def decorador_debug(func):

    def wrapper(*args, **kwargs):
        print(f"=== Ejecutando {func.__name__} ===")
        resultado = func(*args,**kwargs)
        print(f"=== {func.__name__} termino ===")
        return resultado

    return wrapper

# Pruebas
@decorador_debug
def suma(a, b):
    return a + b

@decorador_debug
def saludar(nombre):
    return f"Hola {nombre}"