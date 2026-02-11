from concurrent.interpreters import list_all


class Node:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return f"{self.valor}"
class LinkedList:
    def __init__(self):
        self.head = None

    def agregar(self,valor):
        nodo = Node(valor)
        if self.head is None:
            self.head = nodo
            return
        ultimo = self.head
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nodo

    def remover(self,valor):
        if not self.head:
            return
        if self.head.valor == valor:
            self.head = self.head.siguiente
        actual = self.head
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

    def obtener(self,valor):
        actual = self.head
        while actual:
            if actual.valor == valor:
                return actual.valor
            actual = actual.siguiente
        return "Dato no encontrado"

    def iterar(self):
        actual = self.head
        while actual:
            print(actual.valor)
            actual = actual.siguiente

lista = LinkedList()
lista.agregar(4)

print(lista.obtener(3))