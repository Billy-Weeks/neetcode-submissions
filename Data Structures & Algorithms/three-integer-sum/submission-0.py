class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Find 3 integers which == 0 when added. Return 3 intergers
        # May have more than 1 set of 3 to be returned (must be distinct)
        # Add each set of 3 to final return list
        # Math => 0 = A + B + C => -A = B + C (B and C are two "moveable" pointers)
        
        # Sorting list will allow us to move the pointers depending on result of math 
            # (up if too small, down if too large)
        nums.sort()

        # Final return list
        output_list = []
        
        for i in range(0, len(nums)):
            # avoids duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1

            # Loop to check for correct triplets
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                
                # Now to check how close to 0 we are
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output_list.append([nums[i], nums[right], nums[left]])
                    left += 1
                    right -= 1

                    # Inner while loop to check if next integer is the same as previous
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return output_list


