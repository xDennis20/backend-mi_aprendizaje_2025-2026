from abc import ABC,abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self,monto: float) -> float:
        pass

    @abstractmethod
    def validar_datos(self) -> bool:
        pass

    def registrar_transaccion(self,monto:float) -> None:
        print(f"Registrando transaccion de ${monto}")

class TarjetaCredito(MetodoPago):
    def __init__(self,numero_tarjeta: str, cvv: str):
        self.numero_bancaria = numero_tarjeta
        self.cvv = cvv

    def procesar_pago(self,monto: float) -> float:
        self.registrar_transaccion(monto)
        return True

    def validar_datos(self) -> bool:
        return len(self.numero_bancaria) == 16 and len(self.cvv) == 3

class PayPal(MetodoPago):
    def __init__(self,correo: str):
        self.correo = correo

    def procesar_pago(self,monto: float) -> float:
        self.registrar_transaccion(monto)
        return True

    def validar_datos(self) -> bool:
        return "@" in self.correo and "." in self.correo

class Transferencia(MetodoPago):
    def __init__(self,numero_cuenta: str):
        self.numero_cuenta = numero_cuenta

    def procesar_pago(self,monto: float) -> float:
        self.registrar_transaccion(monto)
        return True

    def validar_datos(self) -> bool:
        return 10 <= len(self.numero_cuenta) <= 20