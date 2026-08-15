class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Given a string (possibly multiple words or just one word) check to see if it's 
        # a valid palindrome
        # Palindrome is a word/sentence that reads the same backwards and forwards
        # Thoughts: Need to keep track of beginning and end at the same time
            # Also, need to skip whitespaces, special ascii chars ("!", ",", ".", etc)
            # Can possibly get upper and lower case, so force entire string to lowercase

        # Setup right and left "pointers"
        # Right starts at beginning, left starts at end
        left = 0
        right = len(s) - 1

        # Loops through string until the middle of the string
        while left < right :
            # Check to make sure we are skipping non alphanumeric values
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Actual comparison
            if s[left].lower() != s[right].lower():
                return False
            # When chars are the same, increment left, decrement right
            left += 1
            right -= 1
        
        # If outer loop is broken, then string is palindrome
        return True
                

        



































