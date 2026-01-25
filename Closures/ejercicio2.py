def crear_multiplicador(n:int):
    def multiplicar(x: int):
        return n * x
    return multiplicar


doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
por_diez = crear_multiplicador(10)