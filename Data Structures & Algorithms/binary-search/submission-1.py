# Time to complete: 10 mins


class Solution:
    def bSearch(self, left, right, nums, target):
        # base case
        if left > right:
            return -1
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.bSearch(mid + 1, right, nums, target)
        return self.bSearch(left, mid - 1, nums, target)


    def search(self, nums: List[int], target: int) -> int:
# Prompt: take a list and find a specific targer
# Thoughts: Use divide/conquer to split list into smaller sections (recursion?)
    # Since the list is sorted, we know whether to either grab left or right side

        return self.bSearch(0, len(nums) - 1, nums, target)