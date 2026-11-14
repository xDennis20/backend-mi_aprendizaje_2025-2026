from typing import Protocol

class BaseDeDatosReal:
    def guardar(self, plato: str) -> None:
        print(f"[DB REAL] Guardando pedido {plato}...")

class EmailReal:
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"[EMAIL REAL] Conectando a internet y enviando a {destinatario}...")
        print(f"Mensaje: {mensaje}")

class BaseDeDatosFake:
    def __init__(self):
        self.platos: list[str] = []

    def guardar(self, plato: str) -> None:
        self.platos.append(plato)
        print(f"Plato guardado exitosamente")

class EmailFake:
    def __init__(self):
        self.enviados: list[tuple[str, str]] = []

    def enviar(self, destinatario: str, mensaje: str) -> None:
        self.enviados.append((destinatario, mensaje))

class RepositorioPedidos(Protocol):
    def guardar(self, plato: str) -> None: ...

class NotificadorEmail(Protocol):
    def enviar(self, destinatario: str, mensaje: str) -> None: ...

def registrar_pedido(plato: str, email_cliente: str, db: RepositorioPedidos, email_sender: NotificadorEmail) -> None:
    # Guardar plato en la base de datos
    db.guardar(plato)

    # Enviar correo a cliente
    email_sender.enviar(email_cliente, "Su plato fue registrado")

def test_registrar_pedidos():
    db_fake = BaseDeDatosFake()
    email_fake = EmailFake()
    plato = "ceviche"
    email = "hola@gmail.com"

    registrar_pedido(plato, email, db_fake, email_fake)

    assert plato in db_fake.platos
    assert (email, "Su plato fue registrado") in email_fake.enviados

if __name__ == "__main__":
    test_registrar_pedidos()