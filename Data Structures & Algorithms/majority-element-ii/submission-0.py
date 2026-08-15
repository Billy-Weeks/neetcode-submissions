class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """ Problem: 
                    find elements that appear more than the size of the list
                    divided by 3.
            Thoughts:
                    Use dict with key as value in nums and value as frequency
                    Compare values to len(nums) // 3 to see which are greater
        """

        # Variables: return list, number to compare to, dictionary
        out = []
        comp = len(nums) // 3
        freq = {}

        # iterate through nums list
        # Counts number of times integer is seen
        for num in nums:
            # check to see if num exists, set to 0 if does not
            if num not in freq:
                freq[num] = 0
            # increment value at key + 1
            freq[num] += 1

        # now compare each value to see if more comp
        for key, value in freq.items():
            if value > comp:
                out.append(key)
        
        return out

