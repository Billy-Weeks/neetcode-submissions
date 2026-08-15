class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, value in enumerate(nums):
            searched = target - value
            if searched in my_dict:
                return [my_dict[searched], index]
            
            my_dict[value] = index