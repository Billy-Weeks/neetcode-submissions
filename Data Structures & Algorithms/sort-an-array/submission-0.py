class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Problem: simply sort the list without any built in 'sort' functions
        # Time complexity: O(nlog(n))

        # Thoughts:
            # Can use nested for loops to compare values but that'll be n^2
            # AND increase space complexity
            # Implement divide/conquer?

        # temp list for storing sorted values
        tempList = [0] * len(nums)

        # Helper function
        def mergeSort(left_idx, right_idx):
            # base case
            # first half checks to make sure we haven't "crossed over"
            if right_idx - left_idx <= 0:
                return # nothing needs to be returned

            # find middle of list
            mid = left_idx + ((right_idx - left_idx) // 2)

            # store left side of list
            mergeSort(left_idx, mid)

            # store right side of list
            mergeSort(mid + 1, right_idx)

            # Compare and "combine"
            
            # left/right pointers
            left = left_idx
            right = mid + 1
            tempLeft = left_idx # keeps track of where we're starting to place values in correct spots
            
            # while loop
            while left <= mid and right <= right_idx:
                if nums[left] <= nums[right]:
                    tempList[tempLeft] = nums[left]
                    left += 1

                else:
                    tempList[tempLeft] = nums[right]
                    right += 1
                tempLeft += 1

            # Add any left over left side values
            while left <= mid:
                tempList[tempLeft] = nums[left]
                left += 1
                tempLeft += 1
            
            # Add any left over right side values
            while right <= right_idx:
                tempList[tempLeft] = nums[right]
                right += 1
                tempLeft += 1

            # copy sorted list to nums
            for num in range(left_idx, right_idx + 1):
                nums[num] = tempList[num]


        # initial function call of helper function
        mergeSort(0, len(nums) - 1)

        return nums

