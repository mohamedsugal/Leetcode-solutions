import sys  
sys.path.append('/Users/mohamedali/Documents/Python_Misc')  
from Data_structures.BinaryTree import TreeNode

class Solution: 
    def hasPathSum(self, root, sum): 
        if root is None: 
            return False 
        elif root.leftChild is None and root.rightChild is None and sum - root.data == 0: 
            return True 
        return self.hasPathSum(root.leftChild, sum-root.data) or self.hasPathSum(root.rightChild, sum-root.data)

tree = TreeNode(11)
tree.insert(13)
tree.insert(7)
tree.insert(5)
tree.insert(8)
tree.insert(3)
tree.insert(6)
tree.insert(10)
tree.insert(12)
tree.insert(14)

test1 = Solution()
print(test1.hasPathSum(tree, 26))


