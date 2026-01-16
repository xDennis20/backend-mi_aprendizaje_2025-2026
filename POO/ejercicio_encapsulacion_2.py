class Producto:
    def __init__(self, nombre: str, precio_base: float, stock: int = 0):
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock = stock
        self._descuento = 0.0

    @staticmethod
    def es_numerico(valor: float) -> bool:
        if isinstance(valor,(int,float)):
            return True
        return False

    @staticmethod
    def es_negativo(valor: float) -> bool:
        return valor < 0

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor,str):
            raise TypeError("Error: El tipo de dato debe ser string")
        valor = valor.strip()
        if not valor:
            raise ValueError("Error: Nombre vacio")
        self._nombre = valor

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        if self.es_negativo(valor):
            raise ValueError("Error: El valor no debe ser negativo")
        if not self.es_numerico(valor):
            raise TypeError("Error: Valor no numerico")

        self._precio_base = valor

    @property
    def descuento(self) -> float:
        return self._descuento

    @descuento.setter
    def descuento(self, valor: float) -> None:
        min_valor = 0.0
        max_valor = 1.0
        if not self.es_numerico(valor):
            raise TypeError("Error: Valor no numerico")
        if not (min_valor <= valor <= max_valor):
            raise ValueError("Error: El valor no esta en el rango de (0.0-1.0)")
        self._descuento = valor

    @property
    def precio_final(self) -> float:
        return self.precio_base * (1 - self.descuento)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if self.es_negativo(valor):
            raise ValueError("Error: El valor no debe ser negativo")
        if not self.es_numerico(valor):
            raise TypeError("Error: El valor no numerico")
        self._stock = valor

    @property
    def disponible(self) -> bool:
        return self.stock > 0

    def aplicar_descuento(self, porcentaje: float) -> None:
        if self.descuento + porcentaje > 1.0:
            raise ValueError("El descuento resultante excede del 1.0 (100%)")
        self.descuento += porcentaje

    def vender(self, cantidad: int = 1) -> None:
        if self.es_negativo(cantidad):
            raise ValueError("Error: El valor no debe ser negativo")
        if cantidad > self.stock:
            raise ValueError("Error: No hay suficiente stock")
        self.stock -= cantidad
        pass

    def reabastecer(self, cantidad: int) -> None:
        if self.es_negativo(cantidad):
            raise ValueError("El valor no debe ser negativo")
        self.stock += cantidad

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._precio_base} ({int(self._descuento * 100)}%) - Stock: {self._stock}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre='{self._nombre}', precio_base={self._precio_base}, descuento={self._descuento}, stock={self._stock})"
