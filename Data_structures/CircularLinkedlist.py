class ListNode: 
    def __init__(self, x): 
        self.val = x 
        self.next = None

class CircularLinkedList: 
    def __init__(self): 
        self.head = None

    def insertAtHead(self, x): 
        if self.head is None: 
            self.head = ListNode(x)
            self.head.next = self.head 
        else: 
            node = ListNode(x)
            curr = self.head 
            while curr.next != self.head: 
                curr = curr.next 
            node.next = self.head
            curr.next = node
            self.head = node
    
    def insertAtTail(self, x): 
        if self.head is None: 
            self.head = ListNode(x)
            self.head.next = self.head 
        else: 
            node = ListNode(x)
            curr = self.head 
            while curr.next != self.head: 
                curr = curr.next 
            curr.next = node
            node.next = self.head
    
    def printList(self): 
        curr_node = self.head
        while curr_node: 
            print(curr_node.val, end=' -> ')
            curr_node = curr_node.next 
            if curr_node == self.head: 
                break
        print()



link = CircularLinkedList()


link.insertAtHead(9)
link.insertAtHead(11)
link.insertAtHead(4)
link.insertAtTail(15)

link.printList()
