class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # add/clear/double depending on what the input is
        # create an empty stack/list?
        scores = []

        for operation in operations:
            if operation == "D":
                # double last added score
                double_value = scores[-1] * 2
                # add to stack
                scores.append(double_value)
            elif operation == "+":
                # add previous 2 scores together
                add_value = scores[-1] + scores[-2]
                scores.append(add_value)
            elif operation == "C":
                # remove last element in list
                scores.pop() # can return the value, but not needed here
            else:
                # everything else should be just append to end of list (numbers only)
                # change to "int" to change from string to integer
                scores.append(int(operation))
        # empty return value
        final_add_value = 0
        print(scores) # test print
        
        # iterate over stack, adding each element together
        for score in scores:
            final_add_value += score
        return final_add_value