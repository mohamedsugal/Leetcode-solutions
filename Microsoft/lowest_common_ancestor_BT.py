from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


# pre order: root, left, right
def pre_order(root: TreeNode) -> None:
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.val, end=' ')
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()

    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]

    #
    # for k, v in parent.items():
    #     if v is not None:
    #         print(k.val, v.val)
    #     else:
    #         print(k.val, v)


three = TreeNode(3)
six = TreeNode(6)
eight = TreeNode(8)
two = TreeNode(2)
eleven = TreeNode(11)
nine = TreeNode(9)
five = TreeNode(5)
thirteen = TreeNode(13)
seven = TreeNode(7)

three.left = six
three.right = eight
six.left = two
six.right = eleven
eleven.left = nine
eleven.right = five
eight.right = thirteen
thirteen.left = seven

pre_order(three)
print()

lowest_common_ancestor(three, two, five)
