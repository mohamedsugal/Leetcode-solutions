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
            return insert(root.left, x)
    else: 
        if root.right is None: 
            root.right = TreeNode(x)
        else: 
            return insert(root.right, x)

def inOrderTraversal(root): 
    if root.left: 
        inOrderTraversal(root.left)
    print(root.val, end=' ')
    if root.right: 
        inOrderTraversal(root.right)

def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    sums = 0 
    if root is None: 
        return sums 
    
    queue = [root]

    while queue: 
        current = queue.pop()
        if current: 
            if R >= current.val >= L: 
                sums += current.val
            if current.val > L: 
                queue.append(current.left)
            if current.val < R: 
                queue.append(current.right)
    return sums



t = TreeNode(10)
insert(t, 5)
insert(t, 15)
insert(t, 3)
insert(t, 7)
insert(t, 18)

inOrderTraversal(t)
print()
print(rangeSumBST(t, 7, 15))