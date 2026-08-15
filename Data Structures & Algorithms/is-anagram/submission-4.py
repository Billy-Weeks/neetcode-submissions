class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Problem: Check if two strings contain the same letters (different order)

        # First check: detect whether same length strings, otherwise return False
        # Use a dict (map): Keys = chars, values = counts. 
        # Iterate through first string, adding chars/increasing count
        # Iterate through 2nd string, SUBTRACTING letters. 
            # In 2nd loop, check if count < 0 and return False if it is

        if len(s) != len(t):
            return False

        count = {}

        # Set up counts of letters
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        # Remove counts
        for c in t:
            # Base case where a letter is in t but not s, auto return False
            if c not in count: 
                return False
            count[c] -= 1
            # Check if count is less than 0, return False
            if count[c] < 0:
                return False
        
        # if loop is finished, then anagram is found
        return True