# Time to complete: 15 mins

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set up left and right for "window"
        left = 0
        maxLength = 0 # size of window
        seen = set() # store characters, avoids duplicates

        # iterate through each character in string
        for right in range(len(s)):
            # check to see if starting char has been seen already
            # remove the current s[left] from the seen set then increment left
            while s[right] in seen: # once s[right] gets removed, exit while
                seen.remove(s[left])
                left += 1

            # add s[right] to set
            seen.add(s[right])

            # calculate current length, compare to maxLength
            currLength = right - left + 1
            
            if currLength > maxLength:
                maxLength = currLength

        return maxLength