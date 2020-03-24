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
        print(curr_node.val, "-> ", end="")
        curr_node = curr_node.next
    print()

class Solution:
    def isPalindrome(self, head): 
        slow = head
        fast = head 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
        slow = self.reverseList(slow)
        fast = head 
        while slow: 
            if slow.val != fast.val: 
                return False 
            slow = slow.next 
            fast = fast.next 
        return True 

    def reverseList(self, head): 
        prev_node = None
        curr_node = head 
        while curr_node: 
            temp = curr_node.next 
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        head = prev_node
        return head
        


arr = [1,2,3,3,2,1]
node = ListNode(arr[0])
for i in range(1, len(arr)): 
    insert(node, arr[i])
printList(node)

test = Solution()
print(test.isPalindrome(node))

