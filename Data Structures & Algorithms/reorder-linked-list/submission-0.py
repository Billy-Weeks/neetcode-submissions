# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Problem: reorder a linked list, keeping the original head as head
        # then placing the last of the list in the 2nd position, moving the 
        # original 2nd position into 3rd, etc. 

        # Thoughts: Find the middle, split into 2 halves
        #           Reverse 2nd half
        #           Weave in the reveresed half with the first half
        
        # Find middle using slow/fast
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next # Skip to next one
            fast = fast.next.next # skip 2

        prev, curr = None, slow.next
        slow.next = None

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        