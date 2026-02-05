def servidor_web(cls):
    dict_vistas = {}
    metodos = dir(cls)
    for metodo in metodos:
        if not metodo.startswith("vista_"):
            continue
        funcion_real = getattr(cls,metodo)
        if not callable(funcion_real):
            continue
        dict_vistas["/" + metodo[6:]] = funcion_real
    setattr(cls,"rutas",dict_vistas)
    return cls


@servidor_web
class MiSitio:
    def vista_inicio(self):
        return "🏠 Bienvenido al Home"

    def vista_contacto(self):
        return "📧 Escríbenos al mail"

    def funcion_interna(self):
        return "🕵️‍♂️ Esto es privado, no debería ser una ruta"