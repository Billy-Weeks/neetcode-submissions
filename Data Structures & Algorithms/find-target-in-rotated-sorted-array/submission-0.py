class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(n) method => simply search through list and find value, return index
        # O(log n) => Divide and Conquer?
        
        # Variables: 
            # left pointer set @ beginning index
            # right pointer set @ end of list (len - 1)
        left = 0
        right = len(nums) - 1

        # loop through list until either left passes right or equals right
        while left <= right: 
            # establish midpoint (mid)
            mid = (left + right) // 2

            # edge case: mid = target
            if nums[mid] == target:
                return mid

            # check if left is normal sorted
            if nums[left] <= nums[mid]:
                # then see if target is WITHIN "normal" chunk
                if target >= nums[left] and target < nums[mid]:
                    # brings right pointer into left side
                    right = mid - 1
                else:
                    left = mid + 1 # brings left into right side
            
            # Right side is "normal" sorted
            else:
                # check to see if target within "normal" side
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1 # bring left into right side
                else:
                    right = mid - 1 # bring right into left side
        
        # Edge case: target is not within list (left crosses right)
        return -1
