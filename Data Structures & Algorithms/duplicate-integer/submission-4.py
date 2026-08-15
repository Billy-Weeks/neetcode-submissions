class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Goal:
        #   return True if ANY value appears more than once
        #   return False otherwise
        # Ideas:
        #   nested for loop? O(n^2) <- choose 1 num as "key" and see if it exists later in the list
        #   Use dictionary: key = value from list; value = count? <- too big? We don't need the count
        #   Create a new list? Check if num is already in list, return true if it is, add if it's not
        #       if we get to the end of the loop, then no value exists already, so return false

        test_list = []

        for num in nums:
            if num in test_list:
                return True
            test_list.append(num)
        #   Runs only if we've reach the end of nums and not found a duplicate    
        return False
                