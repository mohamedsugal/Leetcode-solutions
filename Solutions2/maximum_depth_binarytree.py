class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

def inOrderTraversal(root):
    if root.left is not None:
        inOrderTraversal(root.left)
    print(f'{root.val}', end=" ")
    if root.right is not None:
        inOrderTraversal(root.right)

def maxDepth(root):
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        for i in range(len(queue)):
            cur_root = queue.pop(0)
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        
    return depth



#           1
#         /   \
#        4    2
#      / \   / \
#    10  9  5  8
#         /
#        7

t = TreeNode(1)
t.left = TreeNode(4)
t.right = TreeNode(2)
t.left.left = TreeNode(10)
t.left.right = TreeNode(9)
t.right.left = TreeNode(5)
t.right.right = TreeNode(8)
t.right.left.left = TreeNode(7)

inOrderTraversal(t)
print()
print(maxDepth(t))




