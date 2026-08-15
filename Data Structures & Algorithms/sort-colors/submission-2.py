class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Alternate solution

        # set up 3 pointers
        left = 0 # keeps track of the "0" range
        right = len(nums) - 1 # keep track of "2" range
        current = 0 # keeps track of what we're evaluating

        # iterate through list
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            
            elif nums[current] == 1:
                current += 1

            else:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1