"""Problema 23: La caja registradora
Tienes dos diccionarios de información y una lista de pedidos.

stock: Cuántos hay.

precios: Cuánto cuesta cada uno.

pedido: Qué quiere el cliente.
stock = {"Manzana": 10, "Pera": 5}
precios = {"Manzana": 2.0, "Pera": 3.0}
pedido = [("Manzana", 12), ("Pera", 2)] # 12 manzanas (solo hay 10), 2 peras"""


def caja_registradora():
    stock = {"Manzana": 10, "Pera": 5}
    precios = {"Manzana": 2.0, "Pera": 3.0}
    pedido = [("Manzana", 12), ("Pera", 2),("Uva",5)]
    total_pagar = 0
    if not pedido:
        return total_pagar
    for producto,cantidad in pedido:
        if producto in stock:
            precio_unitario = precios.get(producto)
            if stock.get(producto) >= cantidad:
                total_pagar += precio_unitario * cantidad
                stock[producto] -= cantidad
            elif stock.get(producto) > 0:
                total_pagar += precio_unitario * stock.get(producto)
                stock[producto] = 0
            else:
                print(f"Error: No disponemos stock del producto {producto}")
        else:
            print(f"Error: No disponemos de ese producto en nuestro inventario")
    return f"Total a pagar: ${total_pagar}"

print(caja_registradora())