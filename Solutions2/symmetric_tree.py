from typing import List 

class TreeNode: 
    def __init__(self, x): 
        self.val = x 
        self.left = None 
        self.right = None 

def inOrderTraversal(root):
    if root.left is not None: 
        inOrderTraversal(root.left)
    print(root.val, end=' ')
    if root.right is not None: 
        inOrderTraversal(root.right)

def isSymmetric(root: TreeNode) -> bool:
    if root is None: 
        return False 
    return check(root.left, root.right)

def check(left_subtree, right_subtree): 
    if left_subtree is None and right_subtree is None: 
        return True 
    elif left_subtree and right_subtree: 
        return left_subtree.val == right_subtree.val \
                and check(left_subtree.left, right_subtree.right) \
                and check(left_subtree.right, right_subtree.left)
    return False 
    
    
        



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(2)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

# inOrderTraversal(tree)
# print()
print(isSymmetric(tree))
