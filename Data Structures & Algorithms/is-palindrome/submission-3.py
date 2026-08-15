class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step1: normalize string (make all lowercase/uppercase)
        lowerString = s.lower()

        # Step2: Set up two variables to keep track of each end (left/right)
        left = 0
        right = len(lowerString) - 1

        # Step3: iterate over string, making sure to not cross left/right
        while left < right:
            
            # Step3.5: Check for non-alpha numeric characters (skip if found)
            while left < right and not lowerString[left].isalnum():
                left += 1
            while left < right and not lowerString[right].isalnum():
                right -= 1
            
            # Step4: Comparison between left and right. Should be the same
                # Since if it's not we want to return False immediately, we test that case
            if lowerString[left] != lowerString[right]:
                return False
            
            # Step5: Increment left pointer, decrement right pointer
            left += 1
            right -= 1
        
        # Step6: If outer while loop completes, all chars match, palindrome is found
        return True
            