def cache_simple(func):
    cache = {}
    def wrapper():
        if func not in cache:
            resultado = func()
            cache[func] = resultado
        return cache.get(func)
    return wrapper

@cache_simple
def obtener_configuracion():
    print("Consultando BD...")
    return {"tema": "oscuro", "idioma": "es"}