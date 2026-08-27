class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set up index pointer (start at beginning of list)
        index = 0

        # iterate using a while loop, going up to len(nums) - 1
        while index < len(nums) - 1:
            # check if index and index + 1 are the same
            if nums[index] == nums[index + 1]:
                # then need to pop one off
                nums.pop(index)
                # don't increment index because of shifting list
            # if index != index + 1
            else:
                # increment index
                index += 1
        return (len(nums))