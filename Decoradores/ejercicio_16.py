def marca_de_agua(cls):
    setattr(cls,"autor","Patito Inc.")
    return cls

@marca_de_agua
class Documento:
    pass
print(Documento.autor)