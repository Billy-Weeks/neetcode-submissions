# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Take k number of lists and sort them into one linked list
        # Initial thought (doesn't seem to be feasbile): have k number of pointers
            # to the head of each list and compare each head to each other and move
            # them along accordingly
        # Second thought: divide/conquer?
        
        # 1. Setup our trusty dummy node anchor
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Initialize the min-heap
        min_heap = []
        counter = 0  # Tie-breaker for nodes with identical values
        
        # 3. Push the starting head of EVERY list into the heap
        for head in lists:
            if head:
                # We store a tuple: (node_value, unique_id, node_object)
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1
                
        # 4. Process the heap until it's completely empty
        while min_heap:
            # Pop the absolute smallest node currently available
            val, _, smallest_node = heapq.heappop(min_heap)
            
            # Attach it to our final merged list
            curr.next = smallest_node
            curr = curr.next
            
            # If that popped node has a neighbor behind it, push it into the heap!
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, counter, smallest_node.next))
                counter += 1
                
        return dummy.next
        
