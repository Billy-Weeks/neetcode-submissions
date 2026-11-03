class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        # set:
        seen = set()
        
        #sort list
        nums.sort()

        # add first element to list
        seen.add(nums[0])

        #iterate
        for index in range(1, len(nums)):
            if nums[index] in seen:
                return False
            if nums[index] - 1 != nums[index-1]:
                return False
        return True
