def singleton(cls):
    instancias = None
    def wrapper(*args,**kwargs):
        nonlocal  instancias
        if instancias is None:
            nueva_instancia = cls(*args,**kwargs)
            instancias = nueva_instancia
        return instancias
    return wrapper
@singleton
class Config:
    def __init__(self):
        print("Inicializando Config")
        self.setting = "default"