"""Problema 22: Validador de compras
Contexto: Tienes una tienda.

Tienes un "Inventario" (Diccionario: Producto -> Stock disponible).

Un usuario intenta comprar una "Lista de Deseos" (Lista de tuplas: Producto, Cantidad).
Objetivo: Debes recorrer el pedido y generar un Recibo final.

Si hay stock suficiente: Restas del inventario y agregas al recibo "Comprado".

Si no hay suficiente stock: Vendes lo que queda (ej: si pide 12 y hay 10, vendes 10) y agregas nota "Stock parcial".

Si no existe o está agotado: Agregas al recibo "Error: No disponible".
"""

def validador_compras():
    inventario = {
        "Laptop": 5,
        "Mouse": 10,
        "Teclado": 0  # Agotado
    }

    pedido_cliente = [
        ("Laptop", 2),  # Quiere 2 laptops
        ("Mouse", 12),  # Quiere 12 mouses (¡Solo hay 10!)
        ("Teclado", 1),  # Quiere 1 teclado (¡No hay!)
        ("Monitor", 1)  # Quiere un Monitor (¡No existe en inventario!)
    ]
    print("----- FACTURA -----")
    for pedido in pedido_cliente:
        if pedido[0] in inventario:
            if pedido[1] <= inventario.get(pedido[0]):
                inventario[pedido[0]] -= pedido[1]
                print(f"Producto Vendido: {pedido[0]}, C: {pedido[1]}")
            elif inventario.get(pedido[0]) > 0:
                print(f"Stock imparcial en el producto: {pedido[0]} Solo se vendieron {inventario.get(pedido[0])} de {pedido[1]} pedidos")
                inventario[pedido[0]] = 0
            else:
                print(f"Error: No disponemos de stock del producto {pedido[0]}")
        else:
            print(f"Error: No disponemos en nuestro inventario el producto")
validador_compras()