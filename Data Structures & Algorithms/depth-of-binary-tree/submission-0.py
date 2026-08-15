# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Problem: travel down until you can't anymore and then return the deepest you went?
        # Thoughts: Using similar logic of moving down until either root.left or root.right == None
                    # OR not root?
                    # Need a counter to keep tracking of each side (left/right) and compare and
                    # return the max of (left, right) count in each iteration?
                    

        # Variables:
        max_depth = 0
        
        # Base:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left) # left recursive call
        right_depth = self.maxDepth(root.right) # right recursive call

        return (max(left_depth, right_depth) + 1)
                    