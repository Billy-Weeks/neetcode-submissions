# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Helper function
    def valid(self, node, left_bound, right_bound):
        # base
        if not node:
            return True

        # Check to make sure current node.val is within bounds
        # return False if not
        if node.val <= left_bound or node.val >= right_bound:
            return False
        
        #update bounds in their respective function calls
        return self.valid(node.left, left_bound, node.val) and self.valid(node.right, node.val, right_bound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Problem: Verify the given tree is a valid BST
        # Thoughts:
            # Traverse entire tree and check each node?
                # Too slow, nested loops
        
        return self.valid(root, float("-inf"), float("inf"))
    