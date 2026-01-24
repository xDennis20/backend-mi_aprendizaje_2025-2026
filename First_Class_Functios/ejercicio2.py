def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b

operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

def calcular(simbolo:str, a: float | int, b: float |int)  -> float|int:
    if simbolo in operaciones:
        operacion = operaciones.get(simbolo)
        try:
            return operacion(a, b)
        except:
            raise ZeroDivisionError("Error: No se puede dividir a cero")
    raise ValueError("Error: Simbolo desconocido")

print(calcular('+', 5, 3))   # 8
print(calcular('-', 10, 4))  # 6
print(calcular('*', 4, 2))   # 8
print(calcular('/', 10, 2))  # 5.0