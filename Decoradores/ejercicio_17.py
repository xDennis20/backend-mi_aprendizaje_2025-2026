def wrapper_censurador(func):
    def wrapper(*args,**kwargs):
        resultado = func(*args,**kwargs)
        if isinstance(resultado,str):
            return resultado.replace("tonto","****")
        return resultado
    return wrapper
def educado(cls):
    metodos = dir(cls)
    for metodo in metodos:
        if metodo.startswith("__"):
            continue
        funcion_real = getattr(cls,metodo)
        if not callable(funcion_real):
            continue
        funcion_censurada = wrapper_censurador(funcion_real)
        setattr(cls,metodo,funcion_censurada)
    return cls

@educado
class Chat:
    def saludar(self):
        return "Hola amigo"

    def insultar(self):
        return "Eres un tonto y feo"