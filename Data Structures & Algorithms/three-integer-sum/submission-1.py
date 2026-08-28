# Time to complete: 39 mins

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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