class Solution:
    """ Problem: Duplicate given array to a new array
        Thoughts: iterate twice (nested for loop) and add the value?
                    Find length, use that kwnoledge to place it?
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # return list of set size and value * 2 * length
        ans = [0] *2*length
        
        
        # iterate and add to nums
        for index in range(length):
            # add nums[index] to same place of ans
            ans[index] = nums[index]
            # add nums[index] to index + length in ans
            ans[index + length] = nums[index]
        
        # return ans
        return ans





        
        
        