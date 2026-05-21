import asyncio

async def buscar_usuario(id):
    print(f"Buscando usuario {id} en la DB...")
    await asyncio.sleep(1)   # simular consulta a DB
    return {"id": id, "nombre": "Ana"}

async def buscar_posts(usuario_id):
    print(f"Buscando posts del usuario {usuario_id}...")
    await asyncio.sleep(1)   # simular otra consulta
    return ["post 1", "post 2"]

async def obtener_perfil(id):
    usuario = await buscar_usuario(id)     # espera 1 seg
    posts   = await buscar_posts(id)       # espera 1 seg más
    print(f"Usuario: {usuario['nombre']}, Posts: {posts}")

asyncio.run(obtener_perfil(42))