class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ## Optimized method
        # Create blank dictionary---- value will be list of string.
        # Key will be a tuple (immutable) which counts num of times each char appears 
        # ***(similar to isAnagram)
        
        anagram = {} # Empty dictionary

        # Loop over string (s) in outer loop then iterate through each char (c) [inner loop]
        for s in strs:
            count = [0] * 26 # Create list of 26 zeroes (reinitializes each iteration)
            for c in s:
                index = ord(c) - ord('a') # takes ascii values of 'a' and current char to get int index
                count[index] += 1
            # Since keys can't be a list (because lists can change/are mutable) convert to tuple
            key = tuple(count)
            
            # Add to dictionary
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(s)
        
        return list(anagram.values())

        # see which strings are anagrams of other strings
        # and add them to a list. 
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # Need a dictionary of lists to hold.. what's the key?

        
'''
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in anagram:
                anagram[sorted_string].append(s)
            else:
                anagram[sorted_string] = [s]
        
        return list(anagram.values())
            O(n * k log k) <--- unoptimized
        '''
