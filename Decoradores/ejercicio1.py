def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Mensaje antes de la funcion original")
        resultado = func(*args,**kwargs)
        print("Mensaje despues de la funcion original")
        return resultado
    return wrapper

@mi_decorador
def sumar(a:int,b:int) -> int:
    return a + b

print(sumar(2,5))

