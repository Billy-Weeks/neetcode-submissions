# Time to complete: 15 mins

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # start at main folder
        # for each non ../ OR ./, dig down
        # create a stack to keep track of folder changes
        levelStack = []

        # iterate through stack, add non ../ OR ./
        for log in logs:

            if levelStack:
                if log == "../":
                    levelStack.pop() # remove top of stack ()

                elif log == "./":
                    continue
                else:
                    levelStack.append(log) # add file name
            else:
                if log not in ("../", "./"):
                    levelStack.append(log)
                    
        
        return len(levelStack)