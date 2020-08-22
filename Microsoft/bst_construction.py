from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def insert(nums: List[int]) -> TreeNode:
    root = TreeNode(nums[0])
    for node in nums[1:]:
        insert_helper(root, node)
    return root


def insert_helper(root: TreeNode, node: int) -> None:
    parent, current = None, root
    while current is not None:
        parent = current
        if node < current.val:
            current = current.left
        else:
            current = current.right
    if node < parent.val:
        parent.left = TreeNode(node)
    else:
        parent.right = TreeNode(node)


def in_order_traversal(root: TreeNode) -> None:
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val, end=" ")
        root = root.right


def post_order_traversal(root: TreeNode) -> None:
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        temp = stack[-1].right
        if temp is None:
            temp = stack.pop()
            print(temp.val, end=" ")
            while stack and temp == stack[-1].right:
                temp = stack.pop()
                print(temp.val, end=" ")
        else:
            root = temp


def level_order_traversal(root: TreeNode) -> list:
    queue = [root]
    res = []
    while queue:
        curr = queue.pop(0)
        res += [[curr.val]]
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res


# nodes = [8, 3, 10, 1, 6, 4, 7, 14, 13]
# r = insert(nodes)
#
# in_order_traversal(r)
# print()
# post_order_traversal(r)
# print()
# print(level_order_traversal(r))
