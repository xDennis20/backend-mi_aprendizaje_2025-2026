"""PROYECTO: Sistema de Caché Manual (60-90 min)
Objetivo:
Crear una función que "cachee" (guarde) resultados de operaciones costosas para evitar recalcularlas."""
def crear_cache():
    funciones_cache = {}
    misses = 0
    hit = 0
    def ejecutar_con_cache(funcion,*args):
        nonlocal funciones_cache,misses,hit
        clave_cache = funcion.__name__, args
        if clave_cache in funciones_cache:
            hit += 1
            return funciones_cache.get(clave_cache)
        else:
            resultado_funcion = funcion(*args)
            funciones_cache[clave_cache] = resultado_funcion
            misses += 1
            return resultado_funcion

    def estadisticas_cache():
        return {
            "hits": hit,
            "misses": misses,
            "cache_size": len(funciones_cache)
        }
    return ejecutar_con_cache, estadisticas_cache

ejecutar, estadistica = crear_cache()

def calcular_fibonacci(n):
    print(f"Calculando fibonacci({n})...")
    if n <= 1:
        return n
    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

# Test 1: Primera llamada
assert ejecutar(calcular_fibonacci, 5) == 5
print("✅ Test 1 pasado")

# Test 2: Segunda llamada MISMOS argumentos (debe usar caché)
# NO debe imprimir "Calculando fib(5)" de nuevo
resultado = ejecutar(calcular_fibonacci, 5)
assert resultado == 5
print("✅ Test 2 pasado")

# Test 3: Llamada con DIFERENTES argumentos
assert ejecutar(calcular_fibonacci, 10) == 55
print("✅ Test 3 pasado")

# Test 4: Estadísticas correctas
estadisticas = estadistica()
assert estadisticas['hits'] == 1, f"Esperado hits=1, obtenido {estadisticas['hits']}"
assert estadisticas['misses'] == 2, f"Esperado misses=2, obtenido {estadisticas['misses']}"
assert estadisticas['cache_size'] == 2, f"Esperado cache_size=2, obtenido {estadisticas['cache_size']}"
print("✅ Test 4 pasado")
