class ListNode: 
    def __init__(self, x): 
        self.val = x
        self.next = None 

def printList(head): 
    curr_node = head 
    while curr_node: 
        print(f'{curr_node.val}', "-> ", end="")
        curr_node = curr_node.next
    print()

def removeNthFromEnd(head, n): 
    dummy = ListNode(0)
    dummy.next = head 
    slow = dummy
    fast = dummy
    
    for i in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next 
        slow = slow.next 
    slow.next = slow.next.next 
    
    return dummy.next 
    

node = ListNode(4)
node.next = ListNode(1)
node.next.next = ListNode(5)
node.next.next.next = ListNode(9)
printList(node)
removeNthFromEnd(node, 4)
printList(node)
