class ListNode(object): 
    def __init__(self, x): 
        self.val = x 
        self.next = None 

def insert(head, x):
    new_node = ListNode(x)
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    
def printList(head): 
    curr = head 
    while curr: 
        print(curr.val, end=" -> ")
        curr = curr.next 

class Solution:
    def removeElements(self, head: ListNode, x: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head 
        prev, curr = dummy_head, head 
        while curr: 
            if curr.val == x: 
                prev.next = curr.next 
            else: 
                prev = curr
            curr = curr.next 
        return dummy_head.next 
        

# 1->2->6->3->4->5->6
l = ListNode(1)
insert(l, 2)
insert(l, 6)
insert(l, 3)
insert(l, 4)
insert(l, 5)
insert(l, 6)
printList(l)
print()

t = Solution()
r = t.removeElements(l, 6)
printList(r)
