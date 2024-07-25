from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        # Initialize previous node as dummy and current node as head
        prev = dummy
        curr = head

        while curr:
            # Check for duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Connect previous node to the node after the last duplicate
                prev.next = curr.next
            else:
                # Move previous node to current node
                prev = curr

            # Move current node to the next node
            curr = curr.next

        return dummy.next


# Helper functions for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Test the deleteDuplicates function
lst = [1,2,3,3,4,4,5]
head = create_linked_list(lst)
sol = Solution()
head = sol.deleteDuplicates(head)
print_linked_list(head)
