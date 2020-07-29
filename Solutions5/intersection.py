class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None


def insert(nums):
    head = LinkedList(nums[0])
    for node in nums[1:]:
        insert_helper(head, node)
    return head


def insert_helper(head, node):
    curr_node = head
    while curr_node.next is not None:
        curr_node = curr_node.next
    curr_node.next = LinkedList(node)


def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print()


def intersection_of_two_lists(list1, list2):
    dummy = LinkedList(-1)
    curr = dummy
    while list1 and list2:
        if list1.val == list2.val:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
            
        list1 = list1.next

    return dummy.next


# 1->2->3->1

nums1 = [1, 2, 3, 4, 6]
nums2 = [2, 4, 6, 8]

# output: 2->4->6
output: [2, 4, 6]

l1 = insert(nums1)
l2 = insert(nums2)

intersection = intersection_of_two_lists(l1, l2)
print_list(intersection)