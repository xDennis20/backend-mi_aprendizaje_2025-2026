from NodoGrafo import NodoGrafo
from collections import deque
import heapq

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

    def buscar_bfs(self,inicio: str, valor: str) -> bool:
        if len(valor.strip()) == 0:
            return False
        visitados = set()
        cola = deque()
        cola.append(self.nodos.get(inicio))
        while cola:
            nodo_actual = cola.popleft()
            print(f"Visitando {nodo_actual.valor}")
            visitados.add(nodo_actual.valor)
            if nodo_actual.valor == valor:
                return True
            for vecino in nodo_actual.vecinos:
                if vecino not in visitados:
                    cola.append(self.nodos.get(vecino))
        return False

    def buscar_dijkstra(self, origen: str, valor: str):
        if len(valor.strip()) == 0:
            return "Error: Valor vacio"

        libreta_costos = {}
        for ciudad in self.nodos:
            libreta_costos[ciudad] = float("inf")
        libreta_costos[origen] = 0
        cola_prioridad = []
        padres = dict()
        contador = 0
        heapq.heappush(cola_prioridad,(0,contador,self.nodos.get(origen)))
        while cola_prioridad:
            peso_actual, contador, nodo_actual = heapq.heappop(cola_prioridad)
            if nodo_actual.valor == valor:
                ruta = []
                paso_actual = valor

                while paso_actual in padres:
                    ruta.append(paso_actual)
                    paso_actual = padres[paso_actual]

                ruta.append(origen)
                ruta.reverse()
                recorrido = " -> ".join(ruta)
                return f"Ruta más corta a {valor}: {recorrido} (Costo total: {peso_actual} horas)"

            for nombre,peso in nodo_actual.vecinos.items():
                peso += peso_actual
                if libreta_costos.get(nombre) > peso:
                    libreta_costos[nombre] = peso
                    padres[nombre] = nodo_actual.valor
                    contador+=1
                    heapq.heappush(cola_prioridad, (peso, contador, self.nodos.get(nombre)))

    def __str__(self):
        return f"Grafo: {self.nodos}"
