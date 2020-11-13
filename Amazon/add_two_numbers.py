from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insert(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    for node in nums[1:]:
        insert_helper(head, node)
    return head


def insert_helper(head: ListNode, node: int) -> None:
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(node)


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        carry = 0
        curr = dummy_head
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //=10
            curr = curr.next
        return dummy_head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = insert(l1)
l2 = insert(l2)

print_list(l1)
print()
print_list(l2)
print()

solution = Solution()
res = solution.addTwoNumbers(l1, l2)
print_list(res)