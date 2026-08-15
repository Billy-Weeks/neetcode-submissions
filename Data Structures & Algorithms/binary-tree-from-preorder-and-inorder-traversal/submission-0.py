# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Problem: Given a list stored in "preorder" and another in "inorder" return root of binary tree
            # Preorder: node, then children are seen
            # inorder: left, root, right
        # Thoughts:
            # Since the preorder begins with the root of the node, index 0 will be the root of tree
            # Inorder: first index is lowest left child. 
        
        #base case:
        if not preorder or not inorder:
            return None
        
        #General case
        
        # Set root of tree to preorder[0]
        root = TreeNode(preorder[0])

        # Find root inside inorder (splits up left/right of tree)
        mid_point = inorder.index(preorder[0])

        # Recursive calls
        root.left = self.buildTree(preorder[1 : mid_point + 1], inorder[ : mid_point]) # left side
        root.right = self.buildTree(preorder[mid_point + 1: ], inorder[mid_point + 1: ]) # right side

        return root
