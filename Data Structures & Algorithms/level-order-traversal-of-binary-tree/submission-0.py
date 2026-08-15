# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Problem: output a list of each level, beginning with root
        # Thoughts:
            # Travel breadth-first search (left to right)
            # Previous nodes
        # return list of list
        output = []

        #base case:
        if not root:
            return output

        # make a queue to 
        queue = collections.deque([root])

        while queue:
            q_len = len(queue) # grabs the current lenght of the queue
            curr_vals = [] # empty list for the values of the current level

            # loop to go through tree and pop parent nodes and
            # grabchildren nodes)
            for _ in range(q_len):
                node = queue.popleft() # pops off index 0 parent node
                curr_vals.append(node.val)

                # Grab children and add to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # add curr_vals to output list
            output.append(curr_vals)

        return output
