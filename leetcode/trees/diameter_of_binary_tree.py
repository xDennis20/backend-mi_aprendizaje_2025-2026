class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_dia = 0

    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diametro_actual = left_height + right_height

            if diametro_actual > self.max_dia:
                self.max_dia = diametro_actual

            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_dia