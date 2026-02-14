class Node:
    def __init__(self,valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self, valor):
        nodo = Node(valor)
        if not self.head:
            self.head = nodo
            self.tail = nodo
            return
        nodo.anterior = self.tail
        self.tail.siguiente = nodo
        self.tail = nodo

    def insertar(self,indice: int,valor):
        if not self.head and indice > 0:
            raise ValueError("Error: Indice fuera de rango")
        nodo = Node(valor)
        if indice == 0:
            if self.head:
                nodo.siguiente = self.head
                self.head.anterior = nodo
                self.head = nodo
            else:
                self.head = nodo
                self.tail = nodo
            return
        contador = 0
        actual = self.head
        while contador < indice:
            if not actual:
                raise IndexError("Error: Indice fuera de rango")
            if contador == (indice - 1):
                nodo.siguiente = actual.siguiente
                nodo.anterior = actual
                if not actual.siguiente is None:
                    actual.siguiente.anterior = nodo
                actual.siguiente = nodo
                if nodo.siguiente is None:
                    self.tail = nodo
            actual = actual.siguiente
            contador += 1

    def iterar_reversa(self):
        ultimo = self.tail
        while ultimo:
            print(ultimo.valor)
            ultimo = ultimo.anterior

    def iterar(self):
        actual = self.head
        while actual:
            print(actual.valor)
            actual = actual.siguiente

lista = ListaDobleEnlazada()
lista.agregar(3)
lista.agregar(9)
lista.agregar(10)
lista.agregar(23)
lista.insertar(4,7)
lista.iterar()