class Solution:

    def encode(self, strs: List[str]) -> str:
        # Take a list of strings and combine them into a string
        # Must keep/maintain order and spacing/special characters

        encoded_strs = ""
        temp_list = []

        for s in strs: # loop through list of strings

            # Find length to use as an indicator of the size of each string
            l = str(len(s)) 

            # Create a list in order to use .join instead of
            # using += and creating a string each time something is added
            temp_list.append(l + "#" + s)

        # Use .join to avoid creating a new list every single time
        encoded_strs = "".join(temp_list)

        print(encoded_strs)
        return encoded_strs

    def decode(self, s: str) -> List[str]:

        # Take in a singular string and return a list of strings
        # Find length of given string to be control variable for while loop
        
        decoded_strs = []
        length_strs = len(s)

        i = 0
        j = 1
        while i < length_strs and j < length_strs:
            # Use indicators: "integer#" to see length (integer) and when
            # length indicator stops and string begins (#)
            while s[j] != "#":
                j += 1
            # j sits at "#"
            # grab just the integer value using i and j
            length_s = int(s[i : j])
            
            # add the string to the final list 
            decoded_strs.append(s[j + 1 : j + 1 + length_s])
            
            i = j + 1 + length_s 
            j = i + 1
            
        return decoded_strs
