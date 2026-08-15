class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Problem: Take 2 strings and return SHORTEST substring in s, that contains all of t
        # Thoughts: min = len(t). Order of t doesn't have match order in s
        
        # Store t in dict, with letter = key and # of that char = value
        t_dict = {}
        for char in t:
            if char not in t_dict:
                t_dict[char] = 0
            t_dict[char] += 1       
        
        # Now loop through s and see if letters are in t (using t_dict).
        left = 0 # Keeping track of start of window
        s_dict = {} # Keeping track of letters in s AND in t
        found = 0 # Integer variable to compare length of window to distinct chars in t
        min_length = float('inf')# Used to find smallest substring (set to infinity at first)
        min_window = [-1, -1] # Stores left/right indices so correct substring can be returned

        for right in range(len(s)):
            if s[right] in t_dict:
                if s[right] not in s_dict:
                    s_dict[s[right]] = 0
                s_dict[s[right]] += 1
                if s_dict[s[right]] == t_dict[s[right]]:
                    found += 1
            while found == len(t_dict):
                curr_length = right - left + 1

                if curr_length < min_length:
                    min_length = curr_length
                    min_window = [left, right]
                
                left_char = s[left]

                if left_char in t_dict:
                    s_dict[left_char] -= 1
                
                    if left_char in t_dict and s_dict[left_char] < t_dict[left_char]:
                        found -= 1
                left += 1
        return s[min_window[0]: min_window[1] + 1]
