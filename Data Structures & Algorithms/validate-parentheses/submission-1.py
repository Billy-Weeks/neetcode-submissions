class Solution:
    def isValid(self, s: str) -> bool:
        # A string of various types of parentheses is given and we have to return if it's
        # valid or not. 
        # Valid string = where each open parentheses has a corresponding closing parentheses
        # Must also be in correct order. i.e. "([)]" would not be valid

        # Use list as a stack (LIFO)
        # add open parentheses, pop closing parentheses
        test_stack = []

        # Dictionary holds closing parentheses as keys and opening as value for quick check
        mapping = {')': '(',
                    ']': '[',
                    '}': '{'} 

        # loop through string and read opening/closing parentheses
        for p in s:
            # Add to stack
            if p in "([{":
                test_stack.append(p)
                print(f"{test_stack[-1]}")
            
            # Pop, if matches last element in list
            elif test_stack and p in ")]}" and test_stack[-1] == mapping[p]:
                test_stack.pop()
            
            # If closing parenthesis, but doesn't match top of stack return false
            else:   
                return False
        return not test_stack

