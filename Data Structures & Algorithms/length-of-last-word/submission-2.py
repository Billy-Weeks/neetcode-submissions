# Time to complete: 20 mins

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # can iterate backwards through string until space after char is met
        # strip off white spaces to make sure we start at a char
        s_stripped = s.strip()
        
        if len(s_stripped) == 1:
            return 1

        # count variable to keep track of num of chars
        count = 0
        # iterate from the end till we get to a space
        for index in range(len(s_stripped) - 1, -1, -1):
            if s_stripped[index] == " ":
                return count
            count += 1

