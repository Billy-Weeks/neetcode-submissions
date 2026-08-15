# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Problem: return true if two trees are exactly the same (roots, children, depth)
        # Thoughts:
            # compare roots? So pre-order traversal?
            # recursively call function and check left/right trees

        # base cases:
        # if both sides walk off the edge of both trees
        if not q and not p:
            return True
        # if one is at the end but the other still has at least 1 child:
        if (not q or not p):
            return False

        # Check if values are NOT equal
        if q.val != p.val:
            return False


        # Main cases:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)