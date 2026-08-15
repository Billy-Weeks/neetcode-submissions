class Solution:
    """ Problem: find the combinations which equal to the given number. 
        Must be contiguous (no gaps)
        Thoughts: while loop to iterate until the end? Have a outside counter to keep track of number of correct subarrays <--- Brute force
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Variables: 
            # out -> number of "correct" subarrays
            # curr -> current sum total
            # prevSum -> dict keeping track of previous sum
        out = 0
        curr = 0
        prevSum = {0: 1}

        # iterate over list, using logic of current sum - k should be the value(s) we need
        for num in nums:
            curr += num
            #difference calculation
            difference = curr - k

            out += prevSum.get(difference, 0)
            prevSum[curr] = 1 + prevSum.get(curr, 0)
        
        # return statement
        return out
