# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Problem: Sorting and merging two given lists.
        # Are both lists sorted already? Seems like they are.
        # Can I compare nodes from one list to another? i.e start head of list one and compare to
        # head of list 2? Then depending on the result, move to .next?

        # Variables: Need curr, head, 

        # 1. Setup a dummy node to avoid edge cases with empty lists
        dummy = ListNode()
        curr = dummy
        
        # 2. While BOTH lists still have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            # Move our current pointer forward on the merged list
            curr = curr.next
            
        # 3. If one list runs out early, simply attach the remainder of the other
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        # Return the start of our new list (skipping the dummy node itself)
        return dummy.next