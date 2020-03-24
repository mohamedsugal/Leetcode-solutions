from typing import List 

class TreeNode: 
    def __init__(self, x): 
        self.val = x 
        self.left = None 
        self.right = None 
    
def inOrderTraversal(root): 
    if root.left is not None: 
        inOrderTraversal(root.left)
    print(root.val, end=" ")
    if root.right is not None: 
        inOrderTraversal(root.right)
        

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: 
            return []
        paths = []
        self.dfs(root, "", paths)
        return paths
    
    def dfs(self, root, path, paths): 
        path += str(root.val)
        if not root.left and not root.right: 
            paths.append(path)
        if root.left: 
            self.dfs(root.left, path+"->", paths)
        if root.right: 
            self.dfs(root.right, path+"->", paths)
    
    def binaryTreePathsStack(self, root: TreeNode) -> List[str]: 
        if not root: 
            return []
        paths = []
        stack = [(root, str(root.val))]
        while stack: 
            node, path = stack.pop()
            if not node.left and not node.right: 
                paths.append(path)
            if node.left: 
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right: 
                stack.append((node.right, path + "->" + str(node.right.val)))
        return paths
                
#            1
#          /  \
#         2   3
#       / \    \
#      8  5    7 
# paths = ["1->2->8", "1->2->5", "1->3->7"]

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.left.left = TreeNode(8)
tree.right.right = TreeNode(7)

inOrderTraversal(tree)
print()

n = Solution()
print(n.binaryTreePathsStack(tree))
