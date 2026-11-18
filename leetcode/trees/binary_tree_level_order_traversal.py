from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"

def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    cola: deque[TreeNode] = deque()
    cola.append(root)
    resultado: list[list[int]] = []

    while cola:
        longitud_nivel = len(cola)
        nivel_actual = []

        for _ in range(longitud_nivel):
            nodo = cola.popleft()
            if nodo:
                nivel_actual.append(nodo.val)
                cola.append(nodo.left)
                cola.append(nodo.right)

        if nivel_actual:
            resultado.append(nivel_actual)

    return resultado