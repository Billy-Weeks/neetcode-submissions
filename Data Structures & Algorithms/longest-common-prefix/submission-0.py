class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        prefix = ""
        first_string = strs[0] # stores first string from list

        for i, char in enumerate(first_string):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char

        return prefix



         