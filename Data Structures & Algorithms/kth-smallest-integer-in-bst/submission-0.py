# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Problem: find the given number smallest value. So if k = 1, find the smallest (bottom of tree?)
        #Thoughts:
            # Since it's a BST, we need to go left. And since we have k, we know we need to stop k levels from bottom
            # How to either A: find depth to subtract. (seems like extra steps) OR B: Save left values into list, grab k element from end?
        
        # Variable to hold list of smallest elements
        small_elements = []

        # Helper recursive function
        def inorderTrav(node):

            # Base case: node has traversed off tree
            if not node:
                return # don't add anything since node doesn't exists

            # General cases:
            inorderTrav(node.left)
            small_elements.append(node.val)
            inorderTrav(node.right)

        # Process small_elements lists to return kth element
        inorderTrav(root)
        print (small_elements)
        return small_elements[k-1]