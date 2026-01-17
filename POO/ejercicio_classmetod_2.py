class Pedido:
    total_pedidos = 0
    ingresos_totales = 0.0

    TIPO_ONLINE = "online"
    TIPO_TIENDA = "tienda"
    TIPO_MAYORISTA = "mayorista"
    TIPOS_VALIDOS = (TIPO_ONLINE, TIPO_TIENDA, TIPO_MAYORISTA)

    def __init__(self, producto: str, cantidad: int, precio_unitario: float, tipo: str):
        if cantidad <= 0 or precio_unitario <= 0:
            raise ValueError("Error: cantidad y precio unitario invalido")
        if not self.validar_tipo(tipo):
            raise ValueError("Error: Tipo invalido")
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.tipo = tipo
        self.descuento = 0.0  # Porcentaje (0.0 - 1.0)
        self.costo_envio = 0.0
        self.confirmado = False
        Pedido.total_pedidos +=1

    @classmethod
    def online(cls, producto: str, cantidad: int, precio_unitario: float,
               codigo_promo: str = None):
        pedido = cls(producto, cantidad, precio_unitario, cls.TIPO_ONLINE)
        pedido.costo_envio = 5.0

        if codigo_promo == "DESC10":
            pedido.descuento = 0.1
        elif codigo_promo == "DESC20":
            pedido.descuento = 0.2
        elif codigo_promo == "ENVIOGRATIS":
            pedido.costo_envio = 0.0

        if pedido.subtotal > 100:
            pedido.costo_envio = 0.0

        return pedido

    @classmethod
    def tienda(cls, producto: str, cantidad: int, precio_unitario: float,
               pago_efectivo: bool = False):
        pedido = cls(producto,cantidad,precio_unitario,Pedido.TIPO_TIENDA)
        if pago_efectivo:
            pedido.descuento = 0.05
            pedido.costo_envio = 0.0
            return pedido
        pedido.costo_envio = 0.0
        return pedido

    @classmethod
    def mayorista(cls, producto: str, cantidad: int, precio_unitario: float):
        if cantidad < 10:
            raise  ValueError("Error: La cantidad es menor de 10")

        pedido = cls(producto,cantidad,precio_unitario,Pedido.TIPO_MAYORISTA)

        if 10 <= cantidad <= 49:
            pedido.descuento = 0.1
            pedido.costo_envio = 0.0
            return pedido

        elif 50 <= cantidad <= 99:
            pedido.descuento = 0.15
            pedido.costo_envio = 0.0
            return pedido

        elif cantidad >= 100:
            pedido.descuento = 0.2
            pedido.costo_envio = 0.0
            return pedido

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

    @property
    def monto_descuento(self) -> float:
        return self.subtotal * self.descuento

    @property
    def total(self) -> float:
        return self.subtotal - self.monto_descuento + self.costo_envio

    @staticmethod
    def validar_tipo(tipo: str) -> bool:
        return tipo in Pedido.TIPOS_VALIDOS

    @staticmethod
    def validar_codigo_promo(codigo: str) -> bool:
        return codigo in ("DESC10", "DESC20", "ENVIOGRATIS")

    @staticmethod
    def validar_str_vacio(valor: str) -> bool:
        if valor is None:
            return True
        valor = valor.strip()
        if not valor:
            return True
        return False

    @staticmethod
    def validar_cantidad_precio(valor: int | float) -> bool:
        if valor <= 0:
            return True
        return False

    def confirmar(self) -> None:
        if hasattr(self,"confirmado") and self.confirmado:
            raise ValueError("Error: El pedido ya esta confirmado")

        self.confirmado = True
        Pedido.ingresos_totales += self.total

    @classmethod
    def obtener_estadisticas(cls) -> dict:
        return {"total_pedidos": Pedido.total_pedidos,
                "ingresos_totales": Pedido.ingresos_totales}

    def __str__(self) -> str:
        return f"Pedido Online: {self.producto} x{self.cantidad} - Total: ${self.total}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(producto='{self.producto}', cantidad={self.cantidad}, precio_unitario={self.precio_unitario})"
