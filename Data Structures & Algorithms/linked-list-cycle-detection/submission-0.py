# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Investigate and return whether a list contains a cycle or not
            # Cycle = when a node points vis .next to a node previous in the list
        # Traverse through list keeping tracking of visited values/nodes and their index (dict?)
        # if curr.next is in visited nodes, return visited index
        # This does take O(n) space because of the dictionary growing in size to the list
        
        # Variables: slow, fast
        slow = head
        fast = head

        # Two "pointers" to traverse in the same direction
        # One pointer moves +1 (slow) and the other moves +2 (fast)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Once/if both pointers are at the same node, there's a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, then there's no cycle
        return False

        