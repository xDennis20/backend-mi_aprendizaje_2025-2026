from abc import ABC,abstractmethod
from dataclasses import dataclass

class Producto(ABC):
    @abstractmethod
    def calcular_impuestos(self):
        pass

@dataclass
class Laptop(Producto):
    marca: str
    precio: float

    def calcular_impuestos(self):
        return self.precio * 0.15