from typing import List
import bst_construction
from collections import deque
TreeNode = bst_construction.TreeNode


class Solution:
    @staticmethod
    def level_order(root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = deque([root]), []
        while queue:
            level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res


r = TreeNode(3)
r.right = TreeNode(20)
r.left = TreeNode(9)
r.right.right = TreeNode(7)
r.right.left = TreeNode(15)

s = Solution()
print(s.level_order(r))
