class Stack:
    def __init__(self):
        self.lista = []

    def push(self,valor):
        self.lista.append(valor)

    def pop(self):
        if not self.lista:
            raise IndexError("Error: Lista vacia")
        return self.lista.pop()

    def peek(self):
        if not self.lista:
            return None
        return self.lista[-1]

    def is_empty(self):
        return len(self.lista) == 0

def validar_signos(signos: str) -> bool:
    stack = Stack()
    all_signos = {"{": "}",
              "(": ")",
              "[": "]"}
    for signo in signos:
        if signo in all_signos:
            stack.push(signo)
        elif signo in all_signos.values():
            if stack.is_empty() or signo != all_signos.get(stack.peek()):
                return False
            stack.pop()
    return stack.is_empty()

print(validar_signos("}"))