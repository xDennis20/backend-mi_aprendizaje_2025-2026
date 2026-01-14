""" EJERCICIO 1: "Sistema de Roles
Contexto:
Simularás un sistema de permisos como en Reddit/Discord/GitHub."""


class Usuario:
    def __init__(self, nombre: str, email: str):
        if not nombre and email:
            raise ValueError("Nombre y email son requeridos")
        self.nombre = nombre
        self.email = email
    def cambiar_email(self, nuevo_email: str) -> None:
        email_seguro = nuevo_email.strip(" ")
        if not email_seguro:
            print("Error: Email vacio")
            return
        if "@" in email_seguro:
            self.email = email_seguro
            print("El cambio de email funciono correctamente")
        else:
            print("Error: Email no valido")

    def ver_perfil(self) -> str:
        return f"Usuario: {self.nombre} ({self.email})"


class Moderador(Usuario):  # Hereda de Usuario
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre,email)
        self.advertencias_dadas = 0

    def advertir_usuario(self, usuario: Usuario) -> None:
        if usuario:
            self.advertencias_dadas +=1
            print(f"El usuario {usuario.nombre} fue advertido por {self.nombre}")
        else:
            print("El usuario a advertir no existe")

class Admin(Moderador):
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre,email)
        self.usuarios_baneados = []

    def banear_usuario(self, usuario: Usuario) -> None:
        if usuario:
            self.usuarios_baneados.append(usuario)
            print(f"El usuario {usuario.nombre} baneado por {self.nombre}")
        else:
            print("El usuario a banear no existe")

    def obtener_estadisticas(self) -> str:
        # TODO: Retorna "Admin {nombre}: {X} advertencias, {Y} baneos"
        return f"Admin {self.nombre}: {self.advertencias_dadas} advertencias, {len(self.usuarios_baneados)} baneos"

usuario = Usuario("Ana", "ana@test.com")
print(usuario.ver_perfil())  # "Usuario: Ana (ana@test.com)"

# Test 2: Moderador hereda y extiende
mod = Moderador("Luis", "luis@test.com")
mod.advertir_usuario(usuario)  # Imprime advertencia
mod.advertir_usuario(usuario)
print(f"Advertencias dadas: {mod.advertencias_dadas}")  # 2

# Test 3: Admin tiene TODO (Usuario + Moderador + propio)
admin = Admin("Carlos", "carlos@test.com")
admin.advertir_usuario(usuario)  # Método heredado de Moderador
admin.banear_usuario(usuario)    # Método propio
print(admin.obtener_estadisticas())

admin.cambiar_email("nuevo@test.com")  # Heredado de Usuario
print(admin.ver_perfil())