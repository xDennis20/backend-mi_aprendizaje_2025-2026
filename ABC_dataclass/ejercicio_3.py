from abc import ABC,abstractmethod

class Notificador(ABC):
    contador_envio = 0

    @abstractmethod
    def enviar(self,enviar: str, destinatario: str) -> bool:
        pass

    @abstractmethod
    def validar_destinatario(self,destinatario: str):
        pass

    @staticmethod
    def registrar_envio(destinatario: str, canal: str) -> None:
        print(f"[LOG] Notificación enviada a {destinatario} por {canal}")

    @staticmethod
    def obtener_total_envios() -> int:
        return Notificador.contador_envio

class EmailNotificador(Notificador):
    def __init__(self,remitente: str):
        self._validar_email(remitente)
        self.remitente = remitente

    @staticmethod
    def _validar_email(email: str):
        if "@" not in email or "." not in email:
            raise ValueError("Email debe contener @ y .")

    def validar_destinatario(self,destinatario: str):
        self._validar_email(destinatario)
        return True

    def enviar(self,enviar: str, destinatario: str) -> bool:
        self.validar_destinatario(destinatario)
        self.registrar_envio(destinatario, "Email")
        Notificador.contador_envio += 1
        print(f"📧 Enviando email a {destinatario} desde {self.remitente}")
        return True

class SMSNotificador(Notificador):
    def __init__(self, codigo_pais: str = "+593"):
        self.codigo_pais = codigo_pais

    @staticmethod
    def _validar_numero(numero: str):
        if not (10 <= len(numero) <= 15):
            raise ValueError("Número debe tener entre 10-15 dígitos")
        if not numero.isdigit():
            raise ValueError("Número debe contener solo dígitos")

    def validar_destinatario(self, destinatario: str):
        self._validar_numero(destinatario)
        return True

    def enviar(self, mensaje: str, destinatario: str) -> bool:
        self.validar_destinatario(destinatario)
        self.registrar_envio(destinatario, "SMS")
        Notificador.contador_envio += 1
        print(f"📱 Enviando SMS a {self.codigo_pais}{destinatario}")
        return True

class PushNotificador(Notificador):
    def __init__(self, app_id: str):
        self.app_id = app_id

    @staticmethod
    def _validar_token(token: str):
        if len(token) != 64:
            raise ValueError("Token debe tener 64 caracteres")
        try:
            int(token, 16)
        except ValueError:
            raise ValueError("Token debe ser hexadecimal")

    def validar_destinatario(self, destinatario: str) -> bool:
        self._validar_token(destinatario)
        return True

    def enviar(self, mensaje: str, destinatario: str) -> bool:
        self.validar_destinatario(destinatario)
        self.registrar_envio(destinatario, "Push")
        Notificador.contador_envio += 1
        print(f"🔔 Enviando push a device {destinatario[:8]}... (app: {self.app_id})")
        return True

class SlackNotificador(Notificador):
    def __init__(self, workspace: str):
        self.workspace = workspace

    @staticmethod
    def _validar_slack(destinatario: str):
        if not (destinatario.startswith("@") or destinatario.startswith("#")):
            raise ValueError("Destinatario debe empezar con @ o #")

    def validar_destinatario(self, destinatario: str) -> bool:
        self._validar_slack(destinatario)
        return True

    def enviar(self, mensaje: str, destinatario: str) -> bool:
        self.validar_destinatario(destinatario)
        self.registrar_envio(destinatario, "Slack")
        Notificador.contador_envio += 1
        print(f"💬 Enviando mensaje a {destinatario} en workspace {self.workspace}")
        return True