class Deque:
    def __init__(self):
        self.lista = []

    def agregar_final(self,valor):
        self.lista.append(valor)

    def agregar_frente(self,valor):
        self.lista.insert(0,valor)

    def remover_final(self):
        if not self.lista:
            raise IndexError("Error: Lista vacia")
        return self.lista.pop()

    def remover_frente(self):
        if not self.lista:
            raise IndexError("Error: Lista vacia")
        return self.lista.pop(0)

    def is_empty(self):
        return len(self.lista) == 0

    def size(self):
        return len(self.lista)

def es_palindromo(palabra: str):
    if not palabra:
        raise ValueError("Error: Palabra vacia")
    deque = Deque()
    for letra in palabra:
        deque.agregar_final(letra)

    while not deque.size() <= 1:
        if deque.remover_frente() != deque.remover_final():
            return False
    return True