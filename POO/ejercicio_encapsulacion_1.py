class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        if not isinstance(saldo_inicial,(float,int)):
            raise TypeError("TypeError: Tipo de dato no valido")
        if saldo_inicial < 0:
            raise ValueError("Error: El valor debe ser mayor a 0")
        self.titular = titular
        self._saldo = saldo_inicial

    @staticmethod
    def es_negativo(valor: float) -> bool:
        return valor < 0

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if not isinstance(valor,(float,int)):
            raise TypeError("TypeError: Tipo de dato no valido")
        if self.es_negativo(valor):
            raise ValueError("Error: El valor no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad: float) -> None:
        if self.es_negativo(cantidad):
            raise ValueError("Error: El valor no puede ser negativo")
        self.saldo += cantidad

    def retirar(self, cantidad: float) -> None:
        if self.es_negativo(cantidad):
            raise ValueError("Error: El valor no puede ser negativo")
        if self.saldo < cantidad:
            raise ValueError("Error: Saldo insuficiente")
        self.saldo -= cantidad

    def __str__(self) -> str:
        return f"Cuenta de {self.titular}: ${self.saldo:.2f}"

# Test 2: Creación válida
cuenta = CuentaBancaria("Ana", 1000)
print(cuenta)  # "Cuenta de Ana: $1000.00"

# Test 3: Depositar
cuenta.depositar(500)
print(f"Saldo después de depositar: ${cuenta.saldo}")  # 1500

# Test 4: Retirar
cuenta.retirar(300)
print(f"Saldo después de retirar: ${cuenta.saldo}")  # 1200

# Test 5: Validaciones
try:
    cuenta.saldo = -500
except ValueError as e:
    print(f"✓ Saldo negativo rechazado: {e}")

try:
    cuenta.retirar(5000)
except ValueError as e:
    print(f"✓ Retiro excesivo rechazado: {e}")

try:
    cuenta.depositar(-100)
except ValueError as e:
    print(f"✓ Depósito negativo rechazado: {e}")