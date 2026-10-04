class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # set up left and right pointers
        left = 0
        right = len(nums) - 1

        while left <= right:
            # grab the middle
            mid = (right + left) // 2
            print(mid)

            # base: mid point == target
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
            