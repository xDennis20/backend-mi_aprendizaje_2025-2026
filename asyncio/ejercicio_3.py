import asyncio

async def consultar_db(tabla, tiempo):
    """Simula una consulta SQL que tarda 'tiempo' segundos"""
    print(f"  → SELECT * FROM {tabla}...")
    await asyncio.sleep(tiempo)
    print(f"  ✓ {tabla} respondió")
    return [f"dato de {tabla}"]

async def procesar_request(usuario_id):
    print(f"\nRequest del usuario {usuario_id} llegó")

    # Consultas independientes → gather
    usuarios, productos, pedidos = await asyncio.gather(
        consultar_db("usuarios", 1),
        consultar_db("productos", 2),
        consultar_db("pedidos", 1.5),
    )

    print(f"Request {usuario_id} completada ✅")
    return {"usuarios": usuarios, "productos": productos}

async def main():
    # 3 requests llegan casi al mismo tiempo
    await asyncio.gather(
        procesar_request(1),
        procesar_request(2),
        procesar_request(3),
    )

asyncio.run(main())