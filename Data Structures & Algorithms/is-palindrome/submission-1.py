class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_string = s.lower()
        left = 0
        right = len(s) - 1

        # Loops through string until the middle of the string
        while left < right :
            # Check to make sure we are skipping non alphanumeric values
            while left < right and not test_string[left].isalnum():
                left += 1
            while left < right and not test_string[right].isalnum():
                right -= 1
            
            # Actual comparison
            if test_string[left] != test_string[right]:
                return False
            # When chars are the same, increment left, decrement right
            left += 1
            right -= 1
        
        # If outer loop is broken, then string is palindrome
        return True