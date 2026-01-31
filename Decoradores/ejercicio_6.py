def cache(func):
    cache_dict = {}
    def wrapper(*args,**kwargs):
        nonlocal cache_dict
        clave_cache = (func.__name__,args,tuple(sorted(kwargs.items())))
        if clave_cache in cache_dict:
            return cache_dict.get(clave_cache)
        resultado = func(*args,**kwargs)
        """Guardamos la funcion como clave con su resultado como valor al dict cache"""
        cache_dict[clave_cache] = resultado
        return resultado
    return wrapper

@cache
def suma(a, b, multiplicador=2):
    print("Resultado")
    return (a + b) * multiplicador

@cache
def fibonacci(n):
    print(f"Calculando fib({n})")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)