class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next


class Solution:
    @staticmethod
    def has_cycle(head: ListNode) -> bool:
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


three = ListNode(3)
# two = ListNode(2)
# zero = ListNode(0)
# neg_four = ListNode(-4)

# three.next = two
# two.next = zero
# zero.next = neg_four
# neg_four.next = two

solution = Solution()
print(solution.has_cycle(three))