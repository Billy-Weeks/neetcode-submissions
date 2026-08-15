class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute force: just compare each char, adding it to a string until it runs into not the same?

        # Step0: base case first-> if first string is empty
        if strs[0] == "":
            return ""
        
        # Step1: Variables-> prefix[str] contains return string, f_string[str] -> holds first string
        prefix = "" # set to empty string so if no chars match, returns empty
        f_string = strs[0]

        # Step2: Iterate over each char in first string
        for index, char in enumerate(f_string):
            # Step3: iterate over each remaining string
            for s in strs[1:]:
                # Step4: compare to char in same position of rest of strings
                if index >= len(s) or s[index] != char:
                    # return current prefix
                    return prefix 
            # Step5: Concatenate (add) char to prefix
            prefix += char
        #Step6: Final prefix return
        return prefix