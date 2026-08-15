# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Step1: define an empty list to append to
        result = []

        # Step2: Helper function to traverse/return the tree
        def deep_search(node):
            # Base case of search
            if not node:
                result.append("N")
                return
            
            # General case
            result.append(str(node.val))

            # Recursive calls
            deep_search(node.left)
            deep_search(node.right)

            # Should I return or append the values OR do both?
            pass # why pass?
        
        # Step3: Initial helper call
        deep_search(root)
        
        # Step4: return list as a string, separated by ","
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        # Step1: split string back into a list of values
        values = data.split(",")

        # Step2: Global Pointer
        self.i = 0

        # Step3: Helper function to build tree back up
        def deep_search():
            # Check current value
            current_value = values[self.i]

            # If current value is pointing to an empty node
            if current_value == "N":
                self.i += 1
                return None
            # If actual value
            # Create node
            output = TreeNode(int(current_value))
            self.i += 1
            output.left = deep_search()
            output.right = deep_search()

            return output
        return deep_search()
