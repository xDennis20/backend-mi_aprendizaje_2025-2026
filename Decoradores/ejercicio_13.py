def verificar_datos(func):
    def wrapper(*args,**kwargs):
        argumentos_sin_self = args[1:]
        for arg in argumentos_sin_self:
            if not isinstance(arg,int):
                raise TypeError("No es un numero entero")

        for kwarg in kwargs.values():
            if not isinstance(kwarg,int):
                raise TypeError("No es un numero entero")
        return func(*args,**kwargs)
    return wrapper

def solo_enteros(cls):
    nombres = dir(cls)
    for nombre in nombres:
        if nombre.startswith("__"):
            continue
        funcion_real = getattr(cls,nombre)
        if not callable(funcion_real):
            continue
        funcion_verificada = verificar_datos(funcion_real)
        setattr(cls,nombre,funcion_verificada)
    return cls


@solo_enteros
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def multiplicar(self, a, b, c):
        return a * b * c

calc = Calculadora()

print(calc.sumar(5, 10))
print(calc.multiplicar(2, 2, 2))