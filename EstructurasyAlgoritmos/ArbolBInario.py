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

def eliminar_valor(valor,node: Nodo):
    #Caso base: Valor no encontrado
    if node is None:
        print("El valor no existe en el arbol")
        return None
    #Caso base: Encontramos el valor
    if node.valor == valor:
        #Caso 1: El nodo es una hoja
        if node.left is None and node.right is None:
            return None

        # Caso 3: El nodo tiene 2 hijos
        if node.left is not None and node.right is not None:
            sucesor = node.right
            while sucesor.left:
                sucesor = sucesor.left
            node.valor = sucesor.valor
            node.right = eliminar_valor(node.valor, node.right)
            return node
        #Caso 2: El nodo tiene un hijo
        if node.right is not None:
            return node.right
        elif node.left is not None:
            return node.left

    #Recorrer arbol
    if node.valor < valor:
        node.right = eliminar_valor(valor, node.right)
    elif node.valor > valor:
        node.left = eliminar_valor(valor, node.left)
    return node