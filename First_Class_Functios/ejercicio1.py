def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def aplicar_operacion(func, x, y):
    return func(x, y)

resultado1 = aplicar_operacion(multiplicar, 5, 3)
resultado2 = aplicar_operacion(dividir, 10, 2)
