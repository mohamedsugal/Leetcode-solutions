from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(nodes: List[int]):
    root = TreeNode(nodes[0])
    for node in nodes[1:]:
        insert_helper(root, node)
    return root


def insert_helper(root, node):
    if node < root.val:
        if root.left is None:
            root.left = TreeNode(node)
        else:
            insert_helper(root.left, node)
    else:
        if root.right is None:
            root.right = TreeNode(node)
        else:
            insert_helper(root.right, node)


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert_helper(root)
        return root

    def invert_helper(self, node):
        if node is None:
            return
        self.invert_helper(node.left)
        self.invert_helper(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp


nodes = [4, 2, 7, 1, 3, 6, 9]
root = insert(nodes)
inorder_traversal(root)
print()
s = Solution()
res = s.invertTree(root)
inorder_traversal(res)
