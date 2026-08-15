class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Problem: Take an index and multiple each other number besides that index and place
            # in output list
        
        # Initialize output list with all 1's (for multiplication later, can't multiply by 0)
        output = [1] * len(nums)

        # Split list into 2 halves (left/right)
        # Tackle left half first

        # initialize left product
        left = 1
        # iterate through list, setting output[index] as left, then multiplying current left by nums[index]
        for index in range(len(nums)):
            output[index] = left
            left *= nums[index]

        # initialize right product
        right = 1
        # iterate from end to beginning (right side)
        for index in range(len(nums) - 1, -1, -1):
            output[index] *= right
            right *= nums[index]
        
        # return output list
        return output
            

            