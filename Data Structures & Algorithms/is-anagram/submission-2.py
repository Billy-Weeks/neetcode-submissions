class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check to see if 2 strings are the same, just letters in different order
        # Means at the min, the strings need to be the same length

        if len(s) != len(t):
            return False

        # Using a map loop through the first string, adding letters as key and value = 1
        # if key already exists (i.e. letter appears multiple times, increment value)
        # 2nd for loop (not nested) iterates over 2nd string, and if letter (key) is found
        # decrement value of that key. 
        # If key is NOT found, then letter isn't in first string, so return False
        # If value is ever < 0, then 2nd string has MORE of that letter, so return False   

        test_dict = {}
        for char in s:
            if char not in test_dict:
                test_dict[char] = 0
            test_dict[char] += 1
        
        # Iterate over 2nd string
        for char in t:
            if char not in test_dict:
                return False
            test_dict[char] -= 1
            if test_dict[char] < 0:
                return False
        return True

        