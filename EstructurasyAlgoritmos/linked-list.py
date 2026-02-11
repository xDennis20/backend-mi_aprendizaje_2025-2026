
class Node:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return f"{self.valor}"
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self,valor):
        nodo = Node(valor)
        if self.head is None:
            self.head = nodo
            self.tail = nodo
            return
        else:
            self.tail.siguiente = nodo
            self.tail = nodo

    def insertar(self,indice:int, valor):
        if not self.head and indice > 0:
            raise IndexError("Error: Indice fuera de rango")
        nodo = Node(valor)
        if indice == 0:
            if self.head:
                viejo_head = self.head
                self.head = nodo
                self.head.siguiente = viejo_head
            else:
                self.head = nodo
                self.tail = nodo
            return
        contador = 0
        actual = self.head
        while contador < indice:
            if not actual:
                raise IndexError("Error: indice fuera de rango")
            if contador == indice - 1:
                nodo.siguiente = actual.siguiente
                actual.siguiente = nodo
                if nodo.siguiente is None:
                    self.tail = nodo
                return
            actual = actual.siguiente
            contador +=1

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
lista.agregar(9)
lista.agregar(30)
lista.agregar(23)
lista.agregar(50)
lista.agregar(3)
lista.insertar(6,12)
lista.iterar()