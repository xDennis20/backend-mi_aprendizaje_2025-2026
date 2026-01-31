def validar_tipo(*tipos_datos):
    def decorador(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(tipos_datos):
                raise TypeError("Error: Faltan parametros")
            i = 0
            for arg, tipo_dato in zip(args, tipos_datos):
                i+=1
                if not isinstance(arg, tipo_dato):
                    raise TypeError(f"El argumento {i} debe ser {tipo_dato.__name__}, recibio {type(arg).__name__}")

            return func(*args, **kwargs)

        return wrapper
    return decorador

@validar_tipo(int,int)
def suma(a, b):
    return a + b