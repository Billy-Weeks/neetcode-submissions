class Solution:

    def encode(self, strs: List[str]) -> str:
        # Problem: Take a list of strings and make them into one long string that can then
            # be decoded back into the same list of strings

        # Thoughts: need to somehow keep track of length of each strings and pass that through
        # Variables: encoded string variable AND list where we can append each string NOT concantanate

        string_encoded = ""
        # Use a list to append strings to each other to avoid creating a new string each time
        temp = [] 

        for s in strs:
            # find length, turn into a str to include in final string
            length = str(len(s))

            # append to list
            temp.append(length + "#" + s) # use "#" to indicate when length stops and string begins
        
        string_encoded = "".join(temp)
        return string_encoded

    def decode(self, s: str) -> List[str]:
        # Problem: Take encoded string and re-populate list of separate strings
        
        # Variables:
            # string_decoded to return list of strings
            # length_str to store length of entire string
            # i, j to keep track of where we're at in the string
        string_decoded = []
        length_str = len(s)
        i = 0
        j = 1

        while i < length_str and j < length_str:
            while s[j] != "#":
                j += 1

            length = int(s[i : j])

            string_decoded.append(s[j + 1 : j + 1 + length])
            
            i = j + 1 + length 
            j = i + 1
            
        return string_decoded
