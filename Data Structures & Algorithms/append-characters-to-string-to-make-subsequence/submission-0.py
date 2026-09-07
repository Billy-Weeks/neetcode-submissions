# Time to complete: 20 mins

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # set up two pointers
        i, j = 0, 0

        # length variables
        length_s = len(s)
        length_t = len(t)

        # iterate through both using a while loop
        while i < length_s and j < length_t:
            if s[i] == t[j]: # check if chars are equal

                # increment both pointers
                i += 1
                j += 1
            else: # skip the char in s string, but stay at same place in t
                i += 1

        # return the difference between length_t and j
        return length_t - j
