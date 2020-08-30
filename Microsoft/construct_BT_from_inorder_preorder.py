from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def construct_binary_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    index = {n: i for i, n in enumerate(inorder)}
    stack = []
    root = None
    temp = None
    for val in preorder:
        if not root:
            root = TreeNode(val)
            stack.append(root)
        else:
            node = TreeNode(val)
            if index[val] < index[stack[-1].val]:
                stack[-1].left = node
            else:
                while stack and index[stack[-1].val] < index[val]:
                    temp = stack.pop()
                temp.right = node
            stack.append(node)
    return root





pre_order = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
in_order = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
construct_binary_tree(pre_order, in_order)
