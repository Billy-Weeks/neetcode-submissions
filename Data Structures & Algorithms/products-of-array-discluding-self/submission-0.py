class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Explain problem:
            # Given an array, return another array consisting of
            # the elements multiplied by each other
            # ex:
                # input: [1, 2, 3, 4]
                # output: [24, 12, 8, 6]
        # Ideas: iterate over array, multiplying each element?

        # Find length of list to avoid checking outside of it
        length_list = len(nums)

        # initialize a list filled with 1's
        output = [1] * length_list

        # initilize left product (since regardless, the first index has no "left product" we use 1)
        left_prod = 1
        for i in range(length_list):
            output[i] = left_prod
            left_prod *= nums[i]

        # initialize right product (same logic)
        right_prod = 1
        # loop backwards
        for i in range(length_list - 1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]
        
        return output
        














