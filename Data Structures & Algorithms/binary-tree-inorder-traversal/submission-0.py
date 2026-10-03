# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order goes all the way down LEFT, back to parent node, right
        # then back up to next level

        # defined result list []
        result = []

        # helper function to handle recursion
        def inorder(node):
            # base case: when we've gone past the tree
            # return nothing but goes back to next call which should be end of tree
            if not node:
                return

            # left function call
            inorder(node.left)
            # when all left is found, begin adding to return list
            result.append(node.val)
            # then go right
            inorder(node.right)
        # initial helper recursion call
        inorder(root)
        return result
            