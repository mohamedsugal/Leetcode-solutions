class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.leftChild is None:
                self.leftChild = TreeNode(value)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = TreeNode(value)
            else:
                self.rightChild.insert(value)

    def inOrderTraversal(self):
        if self.leftChild is not None:
            self.leftChild.inOrderTraversal()
        print(f'{self.data}, ', end="")
        if self.rightChild is not None:
            self.rightChild.inOrderTraversal()

    def minValueNode(self, value):
        current = value
        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def delete(self, value):
        if self is None:
            return None
        if value < self.data:
            self.leftChild = self.leftChild.delete(value)
        elif value > self.data:
            self.rightChild = self.rightChild.delete(value)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            # deleting node with two children
            # first get the inOrder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)
        return self

    def find(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.leftChild is not None:
                return self.leftChild.find(value)
            else:
                return False
        else:
            if self.rightChild is not None:
                return self.rightChild.find(value)
            else:
                return False


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

    def inOrderTraversal(self):
        if self.root is not None:
            self.root.inOrderTraversal()
        print()

    def delete(self, value):
        if self.root is not None:
            return self.root.delete(value)

    def find(self, value):
        if self.root is not None:
            return self.root.find(value)
        else:
            return False
