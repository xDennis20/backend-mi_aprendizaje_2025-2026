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

print("\n=== Test 2: Creación válida ===")
laptop = Producto("Laptop", 1000, 10)
print(laptop)  # "Laptop - $1000.00 (0% desc) - Stock: 10"
print(repr(laptop))

# Test 3: Precio final calculado automáticamente
print("\n=== Test 3: Cálculo automático de precio final ===")
print(f"Precio base: ${laptop.precio_base}")  # 1000
print(f"Descuento: {laptop.descuento * 100}%")  # 0%
print(f"Precio final: ${laptop.precio_final}")  # 1000
laptop.descuento = 0.2  # 20% descuento
print(f"\nDespués de aplicar 20% descuento:")
print(f"Precio final: ${laptop.precio_final}")  # 800 (calculado automáticamente)
print("\n=== Test 4: Intentar modificar precio_final (read-only) ===")
try:
    laptop.precio_final = 500  # Debe fallar
    print("❌ No debería permitir modificar precio_final")
except AttributeError as e:
    print(f"✅ Error esperado: {e}")
print("\n=== Test 5: Property booleana 'disponible' ===")
print(f"¿Disponible? {laptop.disponible}")  # True (stock=10)
laptop.stock = 0
print(f"¿Disponible después de agotar? {laptop.disponible}")  # False
print("\n=== Test 6: Aplicar descuento adicional ===")
laptop.stock = 5  # Restablecer
laptop.descuento = 0.1  # 10%
print(f"Descuento inicial: {laptop.descuento * 100}%")
print(f"Precio: ${laptop.precio_final}")  # 900


print("\n=== Test 8: Vender producto ===")
print(f"Stock inicial: {laptop.stock}")  # 5
laptop.vender(2)
print(f"Stock después de vender 2: {laptop.stock}")  # 3

try:
    laptop.vender(10)  # Más de lo disponible
    print("❌ Debería haber lanzado ValueError (stock insuficiente)")
except ValueError as e:
    print(f"✅ Error capturado: {e}")

print("\n=== Test 9: Reabastecer ===")
laptop.reabastecer(7)
print(f"Stock después de reabastecer +7: {laptop.stock}")  # 10

# Test 10: Cambios dinámicos
print("\n=== Test 10: Precio final se actualiza automáticamente ===")
laptop.precio_base = 1200
print(f"Nuevo precio base: ${laptop.precio_base}")
print(f"descuento: {laptop.descuento}")
print(f"Precio final (con 20% desc): ${laptop.precio_final}")  # 960 (automático)

laptop.descuento = 0.5  # 50% descuento
print(f"Nuevo descuento: {laptop.descuento * 100}%")
print(f"Precio final: ${laptop.precio_final}")  # 600 (automático)