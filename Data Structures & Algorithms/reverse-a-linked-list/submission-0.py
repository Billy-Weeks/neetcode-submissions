# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Problem: Take a singly linked list and reverse the list (so the end of the list becomes the head)
        # Linked lists are lists where only the start is known and 
        # then each node is "linked" to the one next in the list ('next')
        # We know we're at the end of the list when next == Null

        # Ideas: Store head into temp variable. point previous tail/end.next to it's previous
            # Keep doing that till we reach head. Set head.next to null. Then set previous tail/end to head.
            # Return head

        # Vairables:
        # temp = stores the current's next location, prev = stores the previous node to attach later (starts at None)
        # curr = stores the current node (start off at head)

        prev = None
        curr = head

        while curr:
            temp = curr.next

            curr.next = prev

            prev = curr

            curr = temp

        return prev