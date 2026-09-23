class Node:
    def __init__(self, clave, value):
        self.value = value
        self.siguiente = None
        self.anterior = None
        self.clave = clave

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.siguiente = self.tail
        self.tail.anterior = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        r_nodo = self.cache[key]
        self.remover(r_nodo)
        self.insertar(r_nodo)
        return r_nodo.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                nodo_eliminar = self.head.siguiente
                self.remover(nodo_eliminar)
                del self.cache[nodo_eliminar.clave]
            nodo_nuevo = Node(key,value)
            self.insertar(nodo_nuevo)
            self.cache[key] = nodo_nuevo
        else:
            nodo_actualizar = self.cache[key]
            nodo_actualizar.value = value
            self.remover(nodo_actualizar)
            self.insertar(nodo_actualizar)

    def insertar(self, nodo: Node):
        self.tail.anterior.siguiente = nodo
        nodo.anterior = self.tail.anterior

        nodo.siguiente = self.tail
        self.tail.anterior = nodo

    @staticmethod
    def remover(nodo: Node):
        nodo.anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = nodo.anterior
