import bst_construction

TreeNode = bst_construction.TreeNode
bst = bst_construction


class Solution:
    @staticmethod
    def is_valid_bst(root: TreeNode) -> bool:
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True


r1 = TreeNode(5)
r1.right = TreeNode(4)
r1.left = TreeNode(1)
r1.right.right = TreeNode(6)
r1.right.left = TreeNode(3)

r2 = bst.insert([2, 1, 3])


def test_solution():
    assert Solution.is_valid_bst(r1) is False
    assert Solution.is_valid_bst(r2) is True
