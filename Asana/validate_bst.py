class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root: TreeNode, node: int):
    if root.val == node:
        return
    if root is None:
        root = node
    else:
        if node < root.val:
            if root.left is None:
                root.left = TreeNode(node)
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = TreeNode(node)
            else:
                insert(root.right, node)


def in_order_traversal(root: TreeNode):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)


def is_valid_bst(root: TreeNode) -> bool:
    stack = []
    left_child = float('-inf')

    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if root.val <= left_child:
            return False
        left_child = root.val
        root = root.right
    return True


tree = TreeNode(2)
tree.left = TreeNode(9)
tree.right = TreeNode(3)

in_order_traversal(tree)
print()
print(is_valid_bst(tree))
