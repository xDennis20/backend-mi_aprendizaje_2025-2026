"""Conexión a Base de Datos Simulada
Contexto: Simularás una conexión a PostgreSQL (sin librerías, todo fake).
Requisitos:

Crea una clase DatabaseConnection que simule conectarse a una BD.
Al crear una instancia, debe guardar:

host (ej: "localhost")
port (ej: 5432)
state (ej: "desconectado")


Implementa métodos:

conectar(): Cambia state a "conectado" y imprime "Conectado a {host}:{port}"
desconectar(): Cambia state a "desconectado"
ejecutar_query(query): Solo funciona si state es "conectado' """



class DatabaseConnection:
    """Esta clase se encarga de la conexion de la base de datos.
    Creamos variables constantes para controlar el conectado y desconectado"""
    CONNECT = "connect"
    DISCONNECT = "disconnect"

    def __init__(self,host: str, port: int):
        """Creamos el constructor que le vamosa pedir al usuario que ingrese el host y el puerto"""
        self.host = host
        self.port = port
        self.state = self.DISCONNECT

    def connect(self) -> None:
        """Se encarga de conectar la base de datos con la variable state del constructor"""
        self.state = self.CONNECT
        print(f"Base de datos Conectada con éxito a {self.host}:{self.port}")

    def disconnect(self) -> None:
        """Se encarga de desconectar la base de datos conla variable state del constructor"""
        self.state = self.DISCONNECT
        print(f"La base de datos fue desconectada")

    def execute_query(self,query:str) -> None:
        """Esta funcion se encarga de ejecutar una query pero dependiendo si la base de datos
        este conectada o desconectada, si esta desconectada rompe el sistema con un error
        mencionando que la base de datos esta desconectada."""
        if self.state == self.CONNECT:
            print(f"Ejecutando: {query}")
            print("Query realizado con exito")
        else:
                raise ConnectionError("Error: Base de datos desconectada")

    def __repr__(self):
        return f"{type(self).__name__}(host='{self.host}', port='{self.port}', state='{self.state}')"

postgresql = DatabaseConnection("localhost", 5432)
postgresql.connect()
print(repr(postgresql))
postgresql.execute_query("SELECT * FROM usuarios")
postgresql.disconnect()
print(repr(postgresql))
postgresql.execute_query("SELECT * FROM usuarios")
