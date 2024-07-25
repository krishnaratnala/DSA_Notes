from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a prehead node that will help simplify the merging process
        prehead = ListNode(-1)

        # Maintain a prev pointer to build the new list
        prev = prehead

        # Iterate as long as both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # At this point, one of the lists is exhausted, attach the remaining list
        prev.next = list1 if list1 is not None else list2

        # The prehead's next pointer points to the merged list
        return prehead.next


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

# Test the mergeTwoLists function
list1 = [1, 2, 4]
list2 = [1, 3, 4]
head1 = create_linked_list(list1)
head2 = create_linked_list(list2)
sol = Solution()
merged_head = sol.mergeTwoLists(head1, head2)
print_linked_list(merged_head)