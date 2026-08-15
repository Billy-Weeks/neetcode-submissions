class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        end_dict = {} # will contain char counts/strings

        for s in strs: # loops through entire strings
            count = [0] * 26 # empty list set with 26 0's (alphabet) 
            for c in s: # loop through each char in string
                index = ord(c) - ord('a') # gets index of char (a = 0, b = 1, etc)
                count[index] += 1 # increments the character count 

            key = tuple(count) # makes count list a tuple (immutable)

            if key not in end_dict: # checks if the key exists already
                end_dict[key] = []
            end_dict[key].append(s)
        
        return list(end_dict.values())
