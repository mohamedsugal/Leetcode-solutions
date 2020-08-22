from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def zig_zag_order(root: TreeNode) -> List[list]:
    queue = deque([root])
    result, direction = [], 1
    while queue:
        levels, size = [], len(queue)
        for i in range(size):
            node = queue.popleft()
            levels.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(levels[::direction])
        direction *= -1
    return result


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
r.right.right = TreeNode(7)

print(zig_zag_order(r))