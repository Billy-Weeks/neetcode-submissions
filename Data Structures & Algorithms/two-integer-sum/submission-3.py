class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Problem: Going through a list of numbers, find the two which added together == target
            # Return indices (not values) of those two numbers from original list

        # Declare empty dict to store index (as key) and number as (as value)
        output = {}

        # iterate through list (using enumeration to grab key and values)
        # Subtract current value from target. Check if result is in output
        # If not then add current into output, move forward.
        # If result is found in output, return two indices

        for key, value in enumerate(nums):
            result = target - value
            if result in output:
                return [output[result], key]
            output[value] = key
        
        