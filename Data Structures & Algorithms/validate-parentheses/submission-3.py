class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p_map = {
            ')' :'(',
            ']' : '[',
            '}' : '{'
        }

        # iterate through string letter (parenthesis by parenthesis)
        for parent in s:

            if parent in '([{':
                stack.append(parent)
            elif stack and parent in ')]}' and stack[-1] == p_map[parent]:
                stack.pop()
            else:
                return False
        return not stack
