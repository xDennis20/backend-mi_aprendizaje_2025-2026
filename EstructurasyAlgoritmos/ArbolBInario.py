class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.valor}"

def pre_orden(node: Nodo):
    if node is None:
        return
    print(node.valor) #1. Imprime el nodo root
    pre_orden(node.left) #2. Recorre a la izquierda
    pre_orden(node.right) #3. Va a recorrer la derecha

def in_orden(node):
    if node is None: return
    in_orden(node.left)     # 1. Ve todo a la izquierda
    print(node.valor)       # 2. Imprime
    in_orden(node.right)    # 3. Ve a la derecha

def post_orden(node):
    if node is None: return
    post_orden(node.left)   # 1. Ve todo a la izquierda
    post_orden(node.right)  # 2. Ve todo a la derecha
    print(node.valor)       # 3. Imprime al final

def agregar_valor(valor, node: Nodo):
    if node is None:
        return Nodo(valor)

    if node.valor < valor:
        node.right = agregar_valor(valor,node.right)
    elif node.valor > valor:
        node.left = agregar_valor(valor,node.left)
    return node

def buscar_valor(valor, node: Nodo) -> bool:
    if node is None:
        return False
    if node.valor == valor:
        return True
    if node.valor < valor:
        return buscar_valor(valor, node.right)
    elif node.valor > valor:
        return buscar_valor(valor, node.left)

raiz = Nodo(10)

raiz = agregar_valor(5, raiz)
raiz = agregar_valor(15, raiz)
raiz = agregar_valor(2, raiz)
raiz = agregar_valor(7, raiz)

print(buscar_valor(7,raiz))