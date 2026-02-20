from pyynl.ynl_gen_c import print_type


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,valor):
        self.queue.append(valor)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Error: Lista Vacia")
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            raise IndexError("Error: Lista Vacia")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

def buscar_partida(jugadores: list):
    if not jugadores:
        return
    cola = Queue()
    lista_temporal_jugadores = []
    for jugador in jugadores:
        cola.enqueue(jugador)
    while not cola.is_empty():
        lista_temporal_jugadores.append(cola.dequeue())
        if len(lista_temporal_jugadores) == 5:
            print(f"Partida encontrada para los jugadores: {lista_temporal_jugadores}")
            lista_temporal_jugadores.clear()
    if lista_temporal_jugadores:
        print(f"Esperando mas jugadores... faltan {5 - len(lista_temporal_jugadores)}")

print(buscar_partida(["Jugador 1","Jugador 2","Jugador 3","Jugador 4","Jugador 5","Jugador 6","Jugador 7",]))


