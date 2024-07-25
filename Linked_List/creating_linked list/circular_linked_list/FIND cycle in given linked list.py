from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Helper functions for testing
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

        if i == pos:
            cycle_node = current

    if cycle_node:
        current.next = cycle_node

    return head

def create_linked_list_without_cycle(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# Test the hasCycle function
sol = Solution()

# Test case 1: Linked list with a cycle
list_with_cycle = create_linked_list_with_cycle([3, 2, 0, -4], 1)
print(sol.hasCycle(list_with_cycle))  # Output: True

# Test case 2: Linked list without a cycle
list_without_cycle = create_linked_list_without_cycle([1, 2])
print(sol.hasCycle(list_without_cycle))  # Output: False
