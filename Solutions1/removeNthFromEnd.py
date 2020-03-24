class ListNode: 
    def __init__(self, x): 
        self.val = x
        self.next = None

def insert(head, x): 
    new_node = ListNode(x)
    if head is None: 
        head = new_node
        return 
    last_node = head 
    while last_node.next: 
        last_node = last_node.next 
    last_node.next = new_node

def printList(head): 
    curr_node = head 
    while curr_node: 
        print(f'{curr_node.val}', "->", end=" ")
        curr_node = curr_node.next 
    print()

def deleteNode(head, position): 
    prev_node = None
    curr_node = head 
    i = 1
    while curr_node and i != position: 
        prev_node = curr_node
        curr_node = curr_node.next 
        i += 1
    if curr_node is None: 
        return 
    prev_node.next = curr_node.next

def removeNthFromEnd(head, n): 
    dummy_head = ListNode(0)
    dummy_head.next = head 
    fast = slow = dummy_head
    
    for i in range(n):
        fast = fast.next 
    while fast and fast.next: 
        fast = fast.next 
        slow = slow.next 
    slow.next = slow.next.next 
    
    return dummy_head.next

node = ListNode(8)
insert(node, 1)
insert(node, 7)
insert(node, 3)
insert(node, 9)
printList(node)
removeNthFromEnd(node, 2)
printList(node)
