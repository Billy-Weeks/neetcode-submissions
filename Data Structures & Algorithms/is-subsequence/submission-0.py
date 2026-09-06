# Time to complete: 48 minutes

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # set two points, i and j to start of strings s and t
        i = 0
        j = 0
        
        # iterate over both strings
        while i < len(s) and j < len(t):
            # compare values at specific indices
            if s[i] == t[j]:
                # found a match, increment i
                i += 1
            # for each pass, always increment j (i is NOT incremented if no match)
            j += 1
        
        # loop exits if either i reaches the end of s or j reaches the end or both
        # valid subsequence is only if the entire length of s has been traversed
        if i == len(s):
            return True
        return False
