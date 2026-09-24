# Time to complete: 15 mins

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # set up an empty "stack"
        mathStack = []

        # list to check for operands
        operators = ["+", "-", "*", "/"]

        # iterate through list
        for token in tokens:

            if token in operators:
                # grab the top 2 from the stack. the "first one" is 2nd
                # ***Important for subtraction operands
                second = mathStack.pop()
                first = mathStack.pop()
                if token == "+":
                    mathStack.append(first + second)
                elif token == "-":
                    mathStack.append(first - second)
                elif token == "*":
                    mathStack.append(first * second)
                elif token == "/":
                    mathStack.append(int(first / second))
            else:
                # see an integer, turn from string to int->add to stack
                mathStack.append(int(token))
        # return the only remaining value in the stack
        return mathStack[0]
