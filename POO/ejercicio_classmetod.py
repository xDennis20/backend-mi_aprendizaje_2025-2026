class Usuario:
    total_usuarios = 0
    usuarios_activos = 0

    def __init__(self, nombre: str, email: str, rol: str = "usuario"):
        if not self.validar_email(email):
            raise ValueError("Error: Email no valido")
        if not self.validar_rol(rol):
            raise ValueError("Error: Rol desconocido")
        Usuario.total_usuarios +=1
        Usuario.usuarios_activos +=1
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.activo = True

    @classmethod
    def desde_dict(cls, datos:dict):
        if not ("nombre" in datos and "email" in datos):
            raise ValueError("Error: Faltan campos requeridos")
        rol = datos.get("rol","usuario")
        return cls(datos["nombre"], datos["email"],rol)

    @classmethod
    def crear_admin(cls, nombre: str, email: str):
        return cls(nombre,email,"admin")

    @classmethod
    def crear_moderador(cls, nombre: str, email: str):
        return cls(nombre,email,"moderador")

    @classmethod
    def obtener_estadisticas(cls) -> dict:
        return {"total": cls.total_usuarios,
                "activos": cls.usuarios_activos,
                "inactivos": cls.total_usuarios - cls.usuarios_activos}

    @staticmethod
    def validar_email(email: str) -> bool:
        return "@" in email and "." in email

    @staticmethod
    def validar_rol(rol: str) -> bool:
        return rol in ("usuario","moderador","admin")

    def desactivar(self) -> None:
        if not self.activo:
            raise ValueError("Error: Este usuario ya esta desactivado")
        self.activo = False
        Usuario.usuarios_activos -=1

    def activar(self) -> None:
        if self.activo:
            raise ValueError("Error: Este usuario ya esta activo")
        self.activo = True
        Usuario.usuarios_activos +=1

    def cambiar_rol(self,rol:str) -> None:
        rol = rol.strip()
        if not rol:
            raise ValueError("Error: Rol Vacio")
        if not self.validar_rol(rol):
            raise ValueError("Error: Rol desconocido")
        self.rol = rol

    def __str__(self) -> str:
        estado = "activo" if self.activo else "inactivo"
        return f"Usuario({self.nombre}, {self.email}, rol={self.rol}, {estado})"

    def __repr__(self) -> str:
        return f"Usuario(nombre='{self.nombre}', email='{self.email}', rol='{self.rol}')"
