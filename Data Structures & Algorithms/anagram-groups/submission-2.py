class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Problem: Find anagrams and store them together in a list of list
        
        # Create blank dict
        output = {}

        # iterate over string in list and THEN each char in string O(n * m)
        for s in strs:
            # Create a new list of 26 0's (alphabet)
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a') # returns ascii index
                count[index] += 1 # increase count at index (keep tracks of # of chars)
            # Set up key to add to output (list CANNOT be keys beacuse they are mutable)
            key = tuple(count)

            # Add to dictionary key to dictionary if not exist AND add s (string)
            if key not in output:
                output[key] = []
            output[key].append(s)
        # Since prompt expects list to be return, cast dictionary into list
        return list(output.values())
            
        
                
            