# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Invert => mirror tree (therefore top root will remain the same, only children swap)
        # Define recursive function to travel down til bottom leaves (no children), then swap
        # Base case: When there is no more root (gone off the bottom of tree)

        if not root:
            return None
        
        # save one child in a temp value to swap
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive call
        self.invertTree(root.left) # Left recursive call
        self.invertTree(root.right) # Right recursive call

        return root 