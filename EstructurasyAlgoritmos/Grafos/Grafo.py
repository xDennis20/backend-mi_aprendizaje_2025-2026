from NodoGrafo import NodoGrafo

class Grafo:
    def __init__(self):
        self.nodos: dict[str,NodoGrafo] = {}

    def agregar_nodo(self, valor: str) -> None:
        nodo = NodoGrafo(valor)
        self.nodos [valor] = nodo

    def conectar_nodos(self, origen: str, destino: str, peso: int) -> None:
        if origen in self.nodos and destino in self.nodos:
            self.nodos.get(origen).agregar_vecino(destino,peso)
        else:
            print("Nodo no encontrado en el grafo")
