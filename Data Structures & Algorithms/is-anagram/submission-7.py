class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base: ensure lengths of strings are equal, otherwise not anagram
        if len(s) != len(t):
            return False
        
        # Create empty hash to count frequencies (char = key, freq = value)
        freq = {}

        # iterate over string s, adding/counting how many of each char
        for c in s:
            # add to dictionary if c (key) is not already in it
            if c not in freq:
                freq[c] = 0
            # increment frequency for each c seen
            freq[c] += 1
        
        # Iterate over t
        for c in t:
            # first check to see if c is NOT in freq, no anagram then
            if c not in freq:
                return False
            freq[c] -= 1 # subtract 1 for each time c is seen
            # check ensures t doesn't have more c than s
            if freq[c] < 0:
                return False # no anagram
        
        # If exited loop, then anagram is found
        return True