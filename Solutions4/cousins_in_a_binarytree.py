class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

def in_order_traversal(root: TreeNode): 
    if root: 
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)

class Solution: 
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        cousins = []
        self.search(root, None, 0, cousins, x, y)
        return cousins[0][0] == cousins[1][0] and cousins[0][1] != cousins[1][1]
    
    def search(self, node, parent, depth, cousins, x, y): 
        if node is None: return 
        
        if node.val == x or node.val == y: 
            cousins.append((depth, parent))
        
        self.search(node.left, node, depth + 1, cousins, x, y)
        self.search(node.right, node, depth + 1, cousins, x, y)


tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.right = TreeNode(7)
# tree.right.right = TreeNode(9)

s = Solution()
print(s.isCousins(tree, 7, 6))

