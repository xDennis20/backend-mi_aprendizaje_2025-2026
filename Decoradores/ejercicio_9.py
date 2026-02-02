def contar_llamadas(func):
    def wrapper(*args,**kwargs):
        resultado = func(*args,**kwargs)
        wrapper.llamadas += 1
        wrapper.ultimo_resultado = resultado
        return resultado
    wrapper.llamadas = 0
    wrapper.ultimo_resultado = None
    return wrapper