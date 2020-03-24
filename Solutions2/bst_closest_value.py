class TreeNode: 
    def __init__(self, x): 
        self.val = x
        self.left = None
        self.right = None 

def insert(root: TreeNode, x: int): 
    if x < root.val: 
        if root.left is None: 
            root.left = TreeNode(x)
        else: 
            insert(root.left, x)
    else: 
        if root.right is None: 
            root.right = TreeNode(x)
        else: 
            insert(root.right, x)

def inOrderTraversal(root: TreeNode): 
    if root.left is not None: 
        inOrderTraversal(root.left)
    print(root.val, end=' ')
    if root.right is not None: 
        inOrderTraversal(root.right)

def closestValue(root: TreeNode, target: int) -> int:
    return closestValueHelper(root, target, float('inf'))

def closestValueHelper(root: TreeNode, target: int, closest: int) -> int: 
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
    
def closestValueIter(root: TreeNode, target: int) -> int: 
    closest = float('inf')
    curr = root 
    while curr is not None: 
        if abs(target - closest) > abs(target - curr.val): 
            closest = curr.val 
        if target < curr.val: 
            curr = curr.left 
        else: 
            curr = curr.right 
    return closest

def hasPathSum(root: TreeNode, sum: int) -> bool:
    if root is None: 
        return False 
    if root.left is None and root.right is None and sum - root.val == 0: 
        return True 
    return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum - root.val)

def branchSums(root: TreeNode) -> list:
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums

def branchSumsHelper(root, curr_sum, sums): 
    if root is None: 
        return 
    curr_sum += root.val 
    if root.left is None and root.right is None: 
        sums.append(curr_sum)
        return 
    branchSumsHelper(root.left, curr_sum, sums)
    branchSumsHelper(root.right, curr_sum, sums)
        


#         4
#        / \
#       2   5
#      / \
#     1   3

tree = TreeNode(4)
insert(tree, 2)
insert(tree, 5)
insert(tree, 1)
insert(tree, 3)

print('BST Tree: ', end="")
inOrderTraversal(tree)
print()
target = 3.714286
print(f'closest value to {target} = {closestValueIter(tree, target)}')

print(branchSums(tree))
