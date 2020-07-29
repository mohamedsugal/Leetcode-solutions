class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class LinkedList(object): 
    def __init__(self): 
        self.head = None 
    
    def insertAtHead(self, x): 
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node

    def insertAtTail(self, x): 
        new_node = ListNode(x)
        if self.head is None: 
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insertAfter(self, key, x): 
        curr_node = self.head
        while curr_node: 
            if curr_node.val == key:
                new_node = ListNode(x)
                new_node.next = curr_node.next 
                curr_node.next = new_node
                return 
            curr_node = curr_node.next
    
    def insertBefore(self, key, x): 
        # inserting before head 
        if self.head.val == key: 
            self.insertAtHead(x)
            return 
        # other cases 
        curr_node = self.head 
        while curr_node.next: 
            if curr_node.next.val == key: 
                new_node = ListNode(x)
                new_node.next = curr_node.next
                curr_node.next = new_node
                return 
            curr_node = curr_node.next
        
    def insertAtPoisition(self, position, x): 
        if position == 0: 
            self.insertAtHead(x)
        i = 0 
        curr_node = self.head 
        while curr_node and i < position - 1: 
            curr_node = curr_node.next 
            i += 1
        if curr_node is None: 
            print("Invalid position!")
        else: 
            new_node = ListNode(x)
            new_node.next = curr_node.next 
            curr_node.next = new_node
    
    def deleteNode(self, x):
        # deleting head 
        if self.head.val == x: 
            self.head = self.head.next 
            return 
        curr_node = self.head
        prev_node = None 
        while curr_node and curr_node.val != x: 
            prev_node = curr_node
            curr_node = curr_node.next 
        if curr_node is None: 
            return 
        prev_node.next = curr_node.next
        curr_node = None
    
    def deleteNodeAtPosition(self, position): 
        # deleting head position 
        if position == 0: 
            self.head = self.head.next 
            return 
        i = 0 
        prev_node = None 
        curr_node = self.head
        while curr_node and i != position: 
            prev_node = curr_node
            curr_node = curr_node.next
            i += 1
        if curr_node is None: 
            return 
        prev_node.next = curr_node.next 
        curr_node = None
    
    def reverseList(self): 
        curr_node = self.head 
        prev_node = None
        while curr_node: 
            temp = curr_node.next 
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp 
        self.head = prev_node
    
    def printList(self): 
        if self.head is None: 
            print("list is empty!")
            return 
        curr_node = self.head
        while curr_node: 
            print(curr_node.val, '-> ', end='')
            curr_node = curr_node.next
        print()

node = LinkedList()
node.insertAtHead(8)
node.insertAtHead(9)

node.printList()
