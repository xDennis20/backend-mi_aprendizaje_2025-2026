from dataclasses import dataclass
from abc import ABC,abstractmethod
from typing import Optional,List

@dataclass
class Usuario:
    id: int
    nombre: str
    email: str

class RepositorioUsuario(ABC):
    @abstractmethod
    def guardar(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, id :int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass

class RepositorioMemoria(RepositorioUsuario):
    def __init__(self):
        self.datos = []

    def guardar(self, usuario: Usuario) -> None:
        self.datos.append(usuario)

    def obtener_por_id(self, id :int) -> Optional[Usuario]:
        for dato in self.datos:
            if dato.id == id:
                return dato
        return None

    def eliminar(self, id: int) -> bool:
        for dato in self.datos:
            if dato.id == id:
                self.datos.remove(dato)
                return True
        return False

class RepositorioSQLSimulado(RepositorioUsuario):
    def guardar(self, usuario: Usuario) -> None:
        print("💾 INSERT INTO users VALUES...")

    def obtener_por_id(self, id :int) -> Optional[Usuario]:
        print("🔍 SELECT * FROM users...")
        return Usuario(3,"dummy","hola@gmail.com")

    def eliminar(self, id: int) -> bool:
        print("Eliminando usuario")
        return True