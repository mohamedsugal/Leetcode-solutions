class TreeNode: 
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

def insert(root, x): 
    if x < root.val: 
        if root.left is None: 
            root.left = TreeNode(x)
        else: 
            insert(root.left, x)
    elif x > root.val: 
        if root.right is None: 
            root.right = TreeNode(x)
        else: 
            insert(root.right, x)
    else: 
        return root

def inOrderTraversal(root): 
    if root.left: 
        inOrderTraversal(root.left)
    print(root.val, end=" ")
    if root.right: 
        inOrderTraversal(root.right)

def closestValue(root, target): 
   return closestValueHelper(root, target, float('inf'))

def closestValueHelper(root, target, closest): 
    if root is None: 
        return closest
    if abs(target - closest) > abs(target - root.val): 
        closest = root.val
    if target < root.val: 
        return closestValueHelper(root.left, target, closest)
    elif target > root.val: 
        return closestValueHelper(root.right, target, closest)
    else: 
        return closest

def closestValueIter(root, target): 
    curr = root
    closest = float('inf')
    while curr is not None: 
        if abs(target - closest) > abs(target - curr.val): 
            closest = curr.val
        if target < curr.val: 
            curr = curr.left 
        else: 
            curr = curr.right 
    return closest


tree = TreeNode(10)
insert(tree, 5)
insert(tree, 15)
insert(tree, 2)
insert(tree, 5)
insert(tree, 1)
insert(tree, 13)
insert(tree, 22)
insert(tree, 14)
inOrderTraversal(tree)
print()

print(closestValue(tree, 13.7))
# print(closestValueIter(tree, 13.7))