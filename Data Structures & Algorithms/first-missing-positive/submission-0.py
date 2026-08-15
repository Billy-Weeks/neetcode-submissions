class Solution:
    """ Problem: find the smallest positive integer NOT in list
        Has to be O(n) time, so no sorting and can't change to set
        constant extra space so that means can't use a positive only 
        list. Must use a comp variable

    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # iterate once and set all negative to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        print(f"first iteration: {nums}")
        # 2nd iteration
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                    print(f"current nums when val - 1 > 0: {nums}")
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
                    print(f"current nums whenn val - 1 == 0: {nums}")
        print(f"2nd iteration: {nums}")
        
        #3rd iteration
        for i in range(1, len(nums) + 1):
            print(f"i is currently: {i}")
            if nums[i - 1] >= 0:
                return i
        # return value greater than length
        return len(nums) + 1

        