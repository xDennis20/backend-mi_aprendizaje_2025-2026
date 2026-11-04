class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    altura_left = max_depth(root.left)
    altura_left+=1
    altura_right = max_depth(root.right)
    altura_right+=1

    return max(1,altura_left,altura_right)




