class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"

def good_nodes(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(node: TreeNode | None, maximo_hallado: int) -> int:
        if not node:
            return 0

        if node.val >= maximo_hallado:
            return 1 + (dfs(node.left, node.val) + dfs(node.right, node.val))

        return 0 + (dfs(node.left, maximo_hallado) + dfs(node.right, maximo_hallado))

    return dfs(root, root.val)