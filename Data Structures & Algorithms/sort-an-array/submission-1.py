# Time to complete: 26 mins
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Step0: Empty list, size of nus
        t_list = [0] * len(nums)

        # Step1: Define helper function to divide
        def sortingMerge(left, right):
            # Step2: when left and right index have "crossed over"
            if right - left <= 0:
                return # return nothing, just go back in the stack
            
            # Step3: find middle of current list
            mid = left + ((right - left) // 2)

            # Step4: recursive function calls (left, then right)
            sortingMerge(left, mid)
            sortingMerge(mid + 1, right)

            # Step5: Comparison checks
            
            # create new pointers with given values
            left_pointer = left
            right_pointer = mid + 1
            temp_start = left # keeps track of where this iteration started

            # Start comparisons
            # while loop
            while left_pointer <= mid and right_pointer <= right:
                if nums[left_pointer] <= nums[right_pointer]:
                    t_list[temp_start] = nums[left_pointer]
                    left_pointer += 1

                else:
                    t_list[temp_start] = nums[right_pointer]
                    right_pointer += 1
                temp_start += 1

            # Add any left over left side values
            while left_pointer <= mid:
                t_list[temp_start] = nums[left_pointer]
                left_pointer += 1
                temp_start += 1
            
            # Add any left over right side values
            while right_pointer <= right:
                t_list[temp_start] = nums[right_pointer]
                right_pointer += 1
                temp_start += 1

            # copy sorted list to nums
            for num in range(left, right + 1):
                nums[num] = t_list[num]
            
        
        # Stepx: Initial function call
        sortingMerge(0, len(nums) - 1)

        # Stepx: return new list
        return nums