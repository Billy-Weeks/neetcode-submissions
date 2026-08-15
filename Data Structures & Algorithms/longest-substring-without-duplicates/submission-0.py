class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Find the longest string within a string that has no repeating characters
        # Return it's length (int)
        # First thoughts of using pointers and moving them along might work, hard to keep track of start

        # Variables
        left = 0
        right = 1
        max_length = 0
        seen = set()

        # loop through string, putting each char in seen
        for right in range(0, len(s)):

            # Check to see if char is already in set
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # add unseen chars to set
            seen.add(s[right])

            # calculate current length and test to see if it's largest
            curr_length = right - left + 1
            if curr_length > max_length:
                max_length = curr_length

        return max_length