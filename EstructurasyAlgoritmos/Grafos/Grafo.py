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

    def buscar_dfs(self,inicio: str,  valor: str, visitados: set = None) -> bool:
        if len(valor.strip()) == 0:
            return False

        if visitados is None:
            visitados = set()

        visitados.add(inicio)
        print(f"Visitando {inicio}")

        if inicio == valor:
            print(f"Encontrado {inicio}")
            return True

        nodo_actual = self.nodos.get(inicio)
        if nodo_actual is None:
            return False

        for vecino in nodo_actual.vecinos:
            if vecino not in visitados:
                if self.buscar_dfs(vecino, valor, visitados):
                    return True
        return False

    def __str__(self):
        return f"Grafo: {self.nodos}"