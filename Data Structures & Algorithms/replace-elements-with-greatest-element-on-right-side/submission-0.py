# Time to complete: 14:28 mins

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # While loop to avoid going over edge?
        # could just compare each value after i to each other? Nested loops: n^2
        # Ending
        # Could use built in min/max and slicing?

        # Variables: 
        newList = [] # empty list to append
        index = 0 # keeps track of position in list
        listLength = len(arr) # prevents re-running length check every time

        # Iterate using while loop, not for loop
        while index < listLength: # prevents going past list end

            # Since last value has no right values, final element of list : -1
            if index + 1 == listLength: 
                newList.append(-1)
                return newList # only place to return, new list is created

            # max value is calculated    
            maxValue = max(arr[index + 1 : ])
            print(f"maxValue = {maxValue}")
            newList.append(maxValue)
            index += 1