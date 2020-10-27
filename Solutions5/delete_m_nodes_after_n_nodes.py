from typing import List


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def insert_at_tail(nodes: List[int]) -> ListNode:
    head = ListNode(nodes[0])
    for node in nodes[1:]:
        insert_helper(head, node)
    return head


def insert_helper(head: ListNode, node: int) -> None:
    while head.next:
        head = head.next
    head.next = ListNode(node)


def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()


class Solution:
    @staticmethod
    def delete_nodes(head: ListNode, m: int, n: int) -> ListNode:
        current = head
        i = 0
        while current:
            if i < m - 1:
                i += 1
            else:
                j = 0
                while j < n and current.next:
                    current.next = current.next.next
                    j += 1
                i = 0
            current = current.next
        return head


list_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_head = insert_at_tail(list_nodes)
print_list(list_head)

s = Solution()
d_nodes = s.delete_nodes(list_head, 2, 3)
print_list(d_nodes)
