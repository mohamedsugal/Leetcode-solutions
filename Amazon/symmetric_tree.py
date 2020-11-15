class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


class Solution:
    # Recursively
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left_subtree, right_subtree):
        if left_subtree is None and right_subtree is None:
            return True
        elif left_subtree and right_subtree:
            return left_subtree.val == right_subtree.val \
                   and self.check(left_subtree.left, right_subtree.right) \
                   and self.check(left_subtree.right, right_subtree.left)
        return False

    # Iteratively
    @staticmethod
    def is_symmetric(root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

solution = Solution()
print(solution.is_symmetric(tree))
