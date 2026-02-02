def retry(max_intentos = 3):
    def decorador(func):
        def wrapper(*args,**kwargs):
            resultado_funcion = func
            for i in range(1, max_intentos + 1):
                try:
                    resultado = resultado_funcion(*args,**kwargs)
                    print(f"Intento {i}/{max_intentos} exitoso")
                    return resultado
                except Exception as e:
                    print(f"Intento {i}/{max_intentos} fallo: Conexion Fallida")
                    print(f"Error: {e}")
                    if i == max_intentos:
                        raise
        return wrapper
    return decorador

intentos = 0
@retry(max_intentos=3)
def contar_intentos():
    global intentos
    intentos += 1
    if intentos < 3:
        raise ValueError("Fallo")
    return "OK"