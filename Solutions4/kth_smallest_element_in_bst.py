class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(arr):
    root = TreeNode(arr[0])
    for node in arr[1:]:
        insert_helper(root, node)
    return root


def insert_helper(root, node):
    if node is None:
        return
    if node < root.val:
        if root.left is None:
            root.left = TreeNode(node)
        else:
            return insert_helper(root.left, node)
    else:
        if root.right is None:
            root.right = TreeNode(node)
        else:
            return insert_helper(root.right, node)


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []
        self.helper(root, nodes)
        print(nodes)
        return nodes[k-1]

    def helper(self, root, nodes):
        if not root:
            return
        self.helper(root.left, nodes)
        nodes.append(root.val)
        self.helper(root.right, nodes)


nodes = [5, 3, 6, 2, 4, None, None, 1]
k = 2
root = insert(nodes)
in_order_traversal(root)
print()
solution = Solution()
print(solution.kthSmallest(root, k))
