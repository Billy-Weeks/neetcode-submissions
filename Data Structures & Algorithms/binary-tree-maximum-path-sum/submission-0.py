# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Problem: Find the path between nodes which leads to the greatest sum
        # Thoughts:
            # Need to be able to keep track of totals, and paths/connections
            # 
        # Global tracking variable
        tracking = [float("-inf")] # Set to lowest possible (negative infinity)

        # Helper function
        def deep_search(node):
            # Base case: no node/empty
            if not node:
                return 0

            # Calls, using max(node, 0) to make sure we arne't sending negative numbers
            left = max(deep_search(node.left), 0) # left recursive call
            right = max(deep_search(node.right), 0) # right recursive call

            # "Arch" (right, left and current node)
            arch = node.val + left + right
            if arch > tracking[0]:
                tracking[0] = arch
            return max(node.val + left, node.val + right) # Calculates the max between going left/right through parent up

        # Initial funciton call
        deep_search(root)
        return tracking[0]
