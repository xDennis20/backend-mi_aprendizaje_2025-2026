import asyncio

async def buscar_usuario(id):
    print("Buscando usuario...")
    await asyncio.sleep(1)
    return {"id": id, "nombre": "Ana"}

async def buscar_posts(id):
    print("Buscando posts...")
    await asyncio.sleep(1)
    return ["post 1", "post 2"]

async def obtener_perfil(id):
    result = await asyncio.gather(buscar_usuario(id), buscar_posts(id))
    print(result)

asyncio.run(obtener_perfil(42))