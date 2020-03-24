class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 
        
def merge_two_linkedlist(L1, L2): 
    dummy_head = Node(0)
    curr = dummy_head
    while L1 and L2: 
        if L1.data < L2.data: 
            curr.next = L1
            L1 = L1.next 
        else: 
            curr.next = L2
            L2 = L2.next 
        curr = curr.next
    

    if L1 is not None: 
        curr.next = L1
    else: 
        curr.next = L2

    return dummy_head.next


L1 = Node(1)
L1.next = Node(4)
L1.next.next = Node(9)


L2 = Node(2)
L2.next = Node(4)
L2.next.next = Node(10)


merged_list = merge_two_linkedlist(L1, L2)
while merged_list: 
    print(merged_list.data, "-> ", end="")
    merged_list = merged_list.next
print()