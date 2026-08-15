class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Create a brand new list of only valid characters, already lowercased
        cleaned = [char.lower() for char in s if char.isalnum()]
        
        # 2. Compare that list to a reversed copy of itself
        return cleaned == cleaned[::-1]