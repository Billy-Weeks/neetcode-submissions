# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Problem: Find and return the root of the two give nodes (p and q)
            # If p is a root and q is a left/right child, return p and vice versa
        # BST means the left tree is less than the root and the right subtree is greater
        # Can use a while loop to traverse the tree, updating the root depending on the
        # decisions: both p.val and q.val are either less or greater than root OR
            # either p.val OR q.val is greater and the other is less

        while root:
            # If p/q are both LESS than root
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root