# Time to complete: 35 minutes

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create empty return string
        string_temp = []
        string_return = ""

        # iterate over list of strings, calculating length of that string and then appending that number PLUS a throwaway character "#" to indicate start of string
        for s in strs:
            length = str(len(s))
            string_temp.append(length + "#" + s)

        string_return = "".join(string_temp)
        
        return string_return



    def decode(self, s: str) -> List[str]:
        # create empty list of strings
        list_strings = []
        # create two pointers which will help with splitting up strings
        start = 0
        end = 1
        length_strings = len(s)

        # iterate through passed in string
        while start < length_strings and end < length_strings:
            # Iterate till we reach "#"
            while s[end] != "#":
                end += 1
            # grab the number which indicates the length of the string    
            lengthOfString = int(s[start : end])

            # update list of strings starting 1 from "#" and ending at lengthOfString
            list_strings.append(s[end + 1 : end + 1 + lengthOfString])

            # update pointers, start needs to be at the end of prev string, end needs to be plus 1 form new start
            start = end + 1 + lengthOfString
            end = start + 1
        
        return list_strings
            
