class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None

    temp_left = root.left
    temp_right = root.right

    root.left = temp_right
    root.right = temp_left

    invertTree(root.left)
    invertTree(root.right)

    return root