class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False; # checks for same length

        # empty dictionary
        test_dict = {}

        # loop to store chars from 's' as keys in test_dict
        for c in s:
            test_dict[c] = test_dict.get(c, 0) + 1

        # loop to check characters in t string

        for c in t:
            if c not in test_dict:
                return False # checks if char in t isn't in s
            test_dict[c] = test_dict[c] - 1

            if test_dict[c] < 0:
                return False # indicates more char c in t
        
        return True
            