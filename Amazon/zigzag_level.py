from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    @staticmethod
    def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, direction = [], 1
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.popleft()
                if direction == -1:
                    level.insert(0, root.val)
                else:
                    level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            direction *= -1
            result.append(level)
        return result


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution.zigzagLevelOrder(tree))
