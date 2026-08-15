class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Take a list of integers and find which two add up to a given target return their indices
        # i.e. nums = [4, 5, 1, 9]; target = 6; 5 and 1 would be the integers, return would be: (1,2)
        # Need to start at first index and then add them to each subsequent index to if i + j == target
        # Nested for loops? 
        
        # Subtract the value from target and see if the next value is the correct pair
        # Dictionary? Allows for O(1) lookups...

        complement_dict = {}     
        for index, value in enumerate(nums):
            sub = target - value
            if sub in complement_dict:
                return [complement_dict[sub], index]
            complement_dict[value] = index
        