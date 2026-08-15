class Solution:
    def validPalindrome(self, s: str) -> bool:
        string_lower = s.lower()
        
        # 1. Wrapped your exact pointer logic into a check function 
        # so we can branch without rewriting your approach.
        def check(b, e):
            while b < e:
                while b < e and not string_lower[b].isalnum():
                    b += 1
                while b < e and not string_lower[e].isalnum():
                    e -= 1
                if string_lower[b] != string_lower[e]:
                    return False
                b += 1
                e -= 1
            return True

        beg = 0 
        end = len(string_lower) - 1 

        while beg < end:
            while beg < end and not string_lower[beg].isalnum():
                beg += 1
            while beg < end and not string_lower[end].isalnum():
                end -= 1
            
            # actual comparisons
            if string_lower[beg] != string_lower[end]:
                # 2. Mismatch found: We drop the 'deleted' flag and 'else' block. 
                # Run your check logic on both possible remaining branches.
                return check(beg + 1, end) or check(beg, end - 1)
            
            # Match found, keep moving inward
            beg += 1
            end -= 1
            
        return True