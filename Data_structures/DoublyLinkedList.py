class Node(object): 
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.prev = None 
    
class DoublyLinkedList(object): 
    def __init__(self): 
        self.head = None 
    
    def insertAtTail(self, data): 
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            new_node.prev = None
            return 
        last_node = self.head
        while last_node.next: 
            last_node = last_node.next 
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = None

    def insertAtHead(self, data): 
        new_node = Node(data)
        if self.head is None: 
            new_node.prev = None
            self.head = new_node
        else: 
            self.head.prev = new_node
            new_node.next = self.head 
            self.head = new_node
            new_node.prev = None



    def print_list(self):
        curr_node = self.head 
        while curr_node: 
            print(curr_node.data, "-> ", end="")
            curr_node = curr_node.next 
        print()


dlist = DoublyLinkedList()
# dlist.insertAtTail(4)
# dlist.insertAtTail(1)
# dlist.insertAtTail(6)
# dlist.insertAtTail(9)
dlist.insertAtHead(11)
dlist.insertAtHead(27)

dlist.print_list()
