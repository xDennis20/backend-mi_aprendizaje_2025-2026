def grito_de_guerra(func):
    def wrapper(*args,**kwargs):
        resultado = func(*args,**kwargs)
        if isinstance(resultado,str):
            return resultado.upper() + "!!!"
        return resultado
    return wrapper

@grito_de_guerra
def susurrar(mensaje):
    return mensaje