class ListNode(object): 
    def __init__(self, x): 
        self.val = x 
        self.next = None 

def insert(head, x):
    new_node = ListNode(x)
    if head is None:
        head = new_node
    else:
        last_node = head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
    return head

def printList(head):
    curr_node = head
    while curr_node is not None:
        print(f'{curr_node.val}', "-> ", end="")
        curr_node = curr_node.next

def addTwoNumbers(l1, l2):
    carry = 0
    dummy_head = ListNode(0)
    dummy_head_ptr = dummy_head
    
    while l1 or l2:
        if l1 is not None: 
            carry += l1.val
            l1 = l1.next
        if l2 is not None: 
            carry += l2.val 
            l2 = l2.next 
        dummy_head_ptr.next = ListNode(carry % 10)
        carry //=10
        dummy_head_ptr = dummy_head_ptr.next 
        
    return dummy_head.next

l1 = ListNode(2)
insert(l1, 4)
insert(l1, 3)
printList(l1)
print()
l2 = ListNode(5)
insert(l2, 6)
insert(l2, 4)
printList(l2)
print()

res = addTwoNumbers(l1, l2)
printList(res)
print()

