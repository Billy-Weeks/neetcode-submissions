class Solution:
    def scoreOfString(self, s: str) -> int:
        # using 'ord' gives the ascii value
        # create sum variable, set to 0
        sum_string = 0

        # iterate over string, using range
        for i in range(len(s) - 1):
            sum_string += abs(ord(s[i]) - ord(s[i + 1]))

        return sum_string


