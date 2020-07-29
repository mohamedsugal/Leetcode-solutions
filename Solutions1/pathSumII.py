class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if node.val < root.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=", ")
        in_order_traversal(root.right)


def path_sum(root, total_sum):
    paths = []
    dfs(root, total_sum, [], paths)
    return paths


def dfs(root, total_sum, current, paths):
    if root is None:
        return

    if root.left is None and root.right is None and total_sum == root.val:
        paths.append(current + [root.val])
        return
    dfs(root.left, total_sum - root.val, current + [root.val], paths)
    dfs(root.right, total_sum - root.val, current + [root.val], paths)


tree = TreeNode(11)
insert(tree, TreeNode(7))
insert(tree, TreeNode(13))
insert(tree, TreeNode(5))
insert(tree, TreeNode(8))
insert(tree, TreeNode(10))
insert(tree, TreeNode(3))
insert(tree, TreeNode(6))
insert(tree, TreeNode(12))
insert(tree, TreeNode(14))

#                 11
#              /    \
#            7      13
#          /  \    /  \
#         5   8   12  14
#       /  \   \
#      3   6   10


in_order_traversal(tree)
print()
print(path_sum(tree, 36))
