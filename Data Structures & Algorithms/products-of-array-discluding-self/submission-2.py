# Time to complete: 10 mins

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize an list size of nums, set all to 1
        out = [1] *len(nums)

        # iterate through list, calculating "left side"
        left = 1
        for index in range(len(nums)):
            out[index] = left
            left *= nums[index]
        # iterate through list, going backwards    
        right = 1
        for index in range(len(nums) - 1, -1, -1):
            out[index] *= right
            right *= nums[index]

        # return
        return out