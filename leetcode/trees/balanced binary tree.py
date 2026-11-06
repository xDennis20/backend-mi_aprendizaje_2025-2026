class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self) -> str:
        return (f"value: {self.val}"
                f"left: {self.left}"
                f"right: {self.right}")

def is_balanced(root: TreeNode | None) -> bool:
    def dfs(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return dfs(root) != -1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

resultado = is_balanced(root)
print(f"¿El árbol está balanceado?: {resultado}")