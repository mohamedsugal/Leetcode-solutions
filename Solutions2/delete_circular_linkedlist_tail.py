class ListNode: 
    def __init__(self, x=None): 
        self.val = x 
        self.next = None

def insert(head=None, x=None): 
    if head is None: 
        head = ListNode(x)
        head.next = head
    else: 
        node = ListNode(x)
        curr = head 
        while curr.next != head: 
            curr = curr.next 
        curr.next = node
        node.next = head
    return head 

def printList(head): 
    curr = head 
    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next 
        if curr == head: 
            break 
    print()

def deleteTail(head): 
    slow = head
    fast = head 
    while fast.next.next != head: 
        slow = slow.next 
        fast = fast.next.next
    
    fast.next.next = None 
    fast.next = head 
    return head 
    


head = None
head = insert(head, 1)
insert(head, 2)
insert(head, 3)
insert(head, 4)

printList(head)

test = deleteTail(head)
printList(test)