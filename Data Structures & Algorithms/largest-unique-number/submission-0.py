class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        # hash to keep track of freq
        freq = {}

        # max holder
        vMax = -1

        # iterate through the list
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1


        for key, value in freq.items():
            if value == 1 and key > vMax:
                vMax = key
  

        return vMax