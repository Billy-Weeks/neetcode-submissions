# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointers
        fast = head
        slow = head

        # find middle
        while fast and fast.next: #(runs fast til the end)
            fast = fast.next.next
            slow = slow.next

        # move backwards
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
                  
        
        return True