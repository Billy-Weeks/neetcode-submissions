class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Since we know the end of the list will have "2" and the beginning will have "0", we can keep pointers at each end to keep track of where we're at
        
        # Pointer variables
        start = 0
        end = len(nums) - 1
        index = 0

        # Iterate through list
        while index <= end:
            if nums[index] == 0:
                # swap with current and beginning part of list
                nums[start], nums[index] = nums[index], nums[start]

                #increment start position and index
                start += 1
                index += 1

            elif nums[index] == 2:
                # swap with current and end part of list
                nums[end], nums[index] = nums[index], nums[end]
                
                # decrement end position (keep index where it's at to check the value that just got moved)
                end -= 1
            else:
                # nums[index] == 1, leave alone, but still move index up
                index += 1
        # return list, hopefully sorted
        return nums
