class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        
        # This tracks the count of the most popular character in our current window
        max_frequent_char_count = 0 
        
        left = 0
        
        for right in range(len(s)):
            # 1. Add the new character to our dictionary
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. Update our tracker for the most frequent character
            max_frequent_char_count = max(max_frequent_char_count, count[s[right]])
            
            # 3. Check if the window is valid
            # Formula: (Total window length) - (Count of most frequent letter) > k
            window_length = right - left + 1
            
            if window_length - max_frequent_char_count > k:
                # The window is invalid. We need to shrink it from the left.
                # First, subtract 1 from the dictionary count for the letter we are leaving behind
                count[s[left]] -= 1
                # Then, physically move the left pointer forward
                left += 1
                
            # 4. Update the overall max length found so far
            # We recalculate right - left + 1 because the window might have shrunk
            max_length = max(max_length, right - left + 1)
            
        return max_length