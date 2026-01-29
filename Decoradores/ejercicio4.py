import time

def decorador_tiempo(func):

    def wrapper(*args, **kwargs):
        tiempo_inicial = time.time()
        resultado = func(*args,**kwargs)
        tiempo_final = time.time()
        tiempo_calculado =  tiempo_final - tiempo_inicial
        args_str = ", ".join([repr(arg) for arg in args])
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k,v in kwargs.items())
        todos_arg = ", ".join(filter(None, [args_str,kwargs_str]))
        print(f"{func.__name__}{todos_arg} tardo {tiempo_calculado:.2f} segundos")
        return resultado
    return wrapper

@decorador_tiempo
def operacion_lenta():
    time.sleep(2)
    return "Terminado"

@decorador_tiempo
def suma_rapida(a, b):
    return a + b