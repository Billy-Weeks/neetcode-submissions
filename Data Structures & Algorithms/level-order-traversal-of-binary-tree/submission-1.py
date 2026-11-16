# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return node values
        # each root get's added to list? then move to root.left, root

        result = []

        def deepSearch(node, depth):
            if not node:
                return None
            
            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)
            deepSearch(node.left, depth + 1)
            deepSearch(node.right, depth + 1)
        
        deepSearch(root, 0)
        return result

