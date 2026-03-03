class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.left = None
        self.right = None

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

raiz = Nodo(10)
hijo_izq = Nodo(5)
hijo_der = Nodo(15)
nieto_izq = Nodo(2)

raiz.left = hijo_izq
raiz.right = hijo_der
hijo_izq.left = nieto_izq
pre_orden(raiz)