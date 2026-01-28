"""PROYECTO: Sistema de Caché Manual (60-90 min)
Objetivo:
Crear una función que "cachee" (guarde) resultados de operaciones costosas para evitar recalcularlas."""
from collections import OrderedDict

def crear_cache(max_size=100):
    funciones_cache = OrderedDict()
    misses = 0
    hit = 0
    def ejecutar_con_cache(funcion,*args):
        nonlocal funciones_cache,misses,hit
        clave_cache = funcion.__name__, args
        if clave_cache in funciones_cache:
            hit += 1
            funciones_cache.move_to_end(clave_cache)
            return funciones_cache.get(clave_cache)
        else:
            resultado_funcion = funcion(*args)
            if len(funciones_cache) >= max_size:
                funciones_cache.popitem(last=False)
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