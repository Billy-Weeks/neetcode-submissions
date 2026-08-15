class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the far right element,
            # the "drop-off" (rotation point) MUST be to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
                
            # Otherwise, the right side is properly sorted, so the minimum 
            # is either the mid element itself, or somewhere to its left.
            else:
                right = mid
                
        # When left and right converge, they point to the absolute minimum.
        return nums[left]