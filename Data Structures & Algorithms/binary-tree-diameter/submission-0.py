# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(root):
            nonlocal result
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)
            
            # check which is larger
            if left + right > result:
                result = left + right
            # return greater out of right and left
            if left > right:
                return 1 + left
            else:
                return 1 + right
        traverse(root)
        return result