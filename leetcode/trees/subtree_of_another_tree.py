class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"valor: {self.val}"

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True

    if (not p and q) or (p and not q):
        return False

    if p.val != q.val:
        return False

    left_equal = is_same_tree(p.left, q.left)
    right_equal = is_same_tree(p.right, q.right)

    return left_equal and right_equal

def is_sub_tree(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    if not subRoot:
        return True

    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return is_sub_tree(root.left, subroot) or is_sub_tree(root.right, subroot)

root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

subroot = TreeNode(2)
subroot.left = TreeNode(4)
subroot.right = TreeNode(5)

print(is_sub_tree(root, subroot))