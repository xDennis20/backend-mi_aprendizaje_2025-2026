from abc import ABC,abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self,monto: float) -> bool:
        pass

    @abstractmethod
    def validar_datos(self) -> bool:
        pass

    def registrar_transaccion(self,monto:float) -> None:
        print(f"Registrando transaccion de ${monto}")

class TarjetaCredito(MetodoPago):
    def __init__(self,numero_tarjeta: str, cvv: str):
        self._validar_numero_tarjeta(numero_tarjeta)
        self._validar_cvv(cvv)
        self.numero_bancaria = numero_tarjeta
        self.cvv = cvv

    @staticmethod
    def _validar_numero_tarjeta(numero_tarjeta: str):
        if len(numero_tarjeta) != 16 and not numero_tarjeta.isdigit():
            raise ValueError("Error: Número de tarjeta debe tener 16 dígitos numéricos")

    @staticmethod
    def _validar_cvv(cvv:str):
        if len(cvv) != 3 and not cvv.isdigit():
            raise ValueError("Error: CVV debe tener 3 digitos numericos")

    def procesar_pago(self,monto: float) -> bool:
        self.registrar_transaccion(monto)
        print(f"💳 Pagando ${monto} con tarjeta ****{self.numero_bancaria[-4:]}")
        return True

    def validar_datos(self) -> bool:
        return True

class PayPal(MetodoPago):
    def __init__(self,correo: str):
        self._validar_correo(correo)
        self.correo = correo

    @staticmethod
    def _validar_correo(correo:str):
        if "@" not in correo and "." not in correo:
            raise ValueError("Error: Correo invalido")

    def procesar_pago(self,monto: float) -> bool:
        self.registrar_transaccion(monto)
        print(f"📧 Pagando ${monto} con PayPal ({self.correo})")
        return True

    def validar_datos(self) -> bool:
        return True

class Transferencia(MetodoPago):
    def __init__(self,numero_cuenta: str):
        self._validar_numero_cuenta(numero_cuenta)
        self.numero_cuenta = numero_cuenta

    @staticmethod
    def _validar_numero_cuenta(numero_cuenta: str):
        if not (10 <= len(numero_cuenta) <= 20) or not numero_cuenta.isdigit():
            raise ValueError("Error: Numero de cuenta invalido")

    def procesar_pago(self,monto: float) -> bool:
        self.registrar_transaccion(monto)
        print(f"🏦 Pagando ${monto} con transferencia (cuenta: {self.numero_cuenta})")
        return True

    def validar_datos(self) -> bool:
        return True