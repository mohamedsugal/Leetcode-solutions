class TreeNode(object): 
    def __init__(self, x): 
        self.val = x
        self.left = None 
        self.right = None

def insert(root, node): 
    if root is None: 
        root = node 
    else: 
        if node.val < root.val: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)
        else: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node)

def inOrderTraversal(root): 
    if root: 
        inOrderTraversal(root.left)
        print(root.val, end=", ")
        inOrderTraversal(root.right)

def hasPathSum(root, sum): 
    if root is None: 
        return False 
    elif root.left is None and root.right is None and sum - root.val == 0: 
        return True 
    return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)



tree = TreeNode(11)
insert(tree, TreeNode(7))
insert(tree, TreeNode(13))
insert(tree, TreeNode(5))
insert(tree, TreeNode(8))
insert(tree, TreeNode(10))
insert(tree, TreeNode(3))
insert(tree, TreeNode(6))
insert(tree, TreeNode(12))
insert(tree, TreeNode(14))

#                 11
#              /    \
#            7      13
#          /  \    /  \
#         5   8   12  14
#       /  \   \
#      3   6   10


inOrderTraversal(tree)
print()
print(hasPathSum(tree, 26))