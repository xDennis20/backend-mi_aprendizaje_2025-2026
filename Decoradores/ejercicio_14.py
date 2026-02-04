def wrapper_retry(func):
    def wrapper(*args,**kwargs):
        max_intentos = 3
        for i in range(1, max_intentos + 1):
            try:
                resultado = func(*args,**kwargs)
                return resultado
            except:
                if i == max_intentos:
                    raise

    return wrapper

def reintentar_todo(cls):
    datos_cls = dir(cls)
    for dato in datos_cls:
        if dato.startswith("__"):
            continue
        funcion_real = getattr(cls,dato)
        if not callable(funcion_real):
            continue
        paso_retry = wrapper_retry(funcion_real)
        setattr(cls,dato,paso_retry)
    return cls

@reintentar_todo
class Conectividad:
    def conectar(self):
        print("📡 Intentando conectar...")
        raise ConnectionError("¡Ups! Se cayó el cable")

c = Conectividad()
try:
    c.conectar()
except ConnectionError:
    print("☠️ Se rindió después de los intentos.")