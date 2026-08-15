# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
             
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Problem: 
            # Check to see if subroot exists completely in root
            # If Subroot ends, then subroot of root should also end at same node(s)
        # Thoughts: 
            # Compare nodes to ensure they are the same, return false if one not root and other root
            # if they are the same, recursively call function so that root.left and subRoot.left are checked
        
        # Base case:
        # If subRoot is empty:
        if not subRoot:
            return True

        # If subRoot, but not root
        if not root:
            return False

        # Main cases
        if self.isSametree(root, subRoot):
            return True
        elif self.isSubtree(root.left, subRoot) or  self.isSubtree(root.right, subRoot):
            return True
        
        return False
    
        
        
        