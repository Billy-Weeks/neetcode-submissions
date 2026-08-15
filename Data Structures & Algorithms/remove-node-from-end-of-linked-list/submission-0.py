# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Problem: remove the node that's n positions from the end of the list
        # Thoughts: Since we don't know the length, we can traverse it once, keeping
                    # count of the length.
                    # Then we subtract n from the count, giving us an index of where to sto
                    # Traverse again, keeping track of previous node (prev) and current
                    # node (curr) but once we get to len - n, we remove it by setting prev.next
                    # to curr.next
                    # Can it be done in one pass?
        # Variables
         # Create temp for head, to become "new" head
        temp = ListNode(0, head)

        left, right = temp, temp
       

        # Move right pointer over n spots
        for _ in range(n):
            right = right.next

        # Move left and right over until right reaches the edge of list (right.next == none)
        while right.next:
            left = left.next
            right = right.next

        # Now left is sitting just before the nth from the end node.
        # Remove node by setting left.next to the nth node's next
        left.next = left.next.next
        
        return temp.next

        