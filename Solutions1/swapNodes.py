class Node(object): 
        def __init__(self, data): 
            self.data = data 
            self.next = None 

class LinkedList(object): 
    def __init__(self): 
        self.head = None 
    
    def insertAtTail(self, val): 
        new_node = Node(val)
        if self.head is None: 
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next is not None: 
            last_node = last_node.next 
        last_node.next = new_node
    
    def printList(self): 
        curr_node = self.head
        while curr_node: 
            print(curr_node.data, "-> ", end="")
            curr_node = curr_node.next
        print()
        

    def swapNodes(self, x, y): 
        if x == y: 
            return 
        prevX = None 
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX
            currX = currX.next
        prevY = None 
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY
            currY = currY.next 
        if currX == None and currY == None: 
            return 
        if prevX != None: 
            prevX.next = currY
        else: 
            self.head = currY
        if prevY != None: 
            prevY.next = currX
        else: 
            self.head = currX
        temp = currX.next 
        currX.next = currY.next 
        currY.next = temp 





myList = LinkedList()
myList.insertAtTail(2)
myList.insertAtTail(4)
myList.insertAtTail(3)
myList.insertAtTail(7)
myList.insertAtTail(9)
myList.printList()
myList.swapNodes(2,7)
myList.printList()