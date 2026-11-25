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
    resultado = []

    while cola:
        long_actual = len(cola)
        nivel_actual = []

        for _ in range(long_actual):
            nodo = cola.popleft()
            nivel_actual.append(nodo.val)
            if nodo.left:
                cola.append(nodo.left)
            if nodo.right:
                cola.append(nodo.right)

        resultado.append(nivel_actual[-1])

    return resultado