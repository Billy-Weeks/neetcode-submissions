# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Bundle the starting node and its absolute boundaries into a tuple
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            # Unpack the bundle from the top of the stack
            node, left_bound, right_bound = stack.pop()
            
            if node.val <= left_bound or node.val >= right_bound:
                return False
            
            
            # --- 2. ADD CHILDREN TO STACK WITH NEW BOUNDS ---
            if node.left:
                # Replace the ??? with the correct floor and ceiling for going left
                stack.append((node.left, left_bound, node.val))
                
            if node.right:
                # Replace the ??? with the correct floor and ceiling for going right
                stack.append((node.right, node.val, right_bound))

        # If the stack empties and we never triggered a False, the tree is valid
        return True
        