from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def pre_order(root: TreeNode) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def in_order(root: TreeNode) -> List[TreeNode]:
    stack = []
    result = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root)
        root = root.right
    return result


def insert(nums: List[int]) -> TreeNode:
    root = TreeNode(nums[0])
    for node in nums[1:]:
        insert_helper(root, node)
    return root


def insert_helper(root: TreeNode, node: int) -> None:
    curr, parent = root, None
    while curr:
        parent = curr
        if node < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    if node < parent.val:
        parent.left = TreeNode(node)
    else:
        parent.right = TreeNode(node)


def lowest_common_ancestor_bst(root: TreeNode, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root


n = [7, 5, 11, 3, 6, 9, 17, 2, 8]
r = insert(n)

res = in_order(r)
for i in res:
    print(i.val, end=" ")
print()
lca = lowest_common_ancestor_bst(r, res[0], res[3])
print(lca.val)
