class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Step0: Check if lengths are the same, return False if not
        if len(s) != len(t):
            return False
        #Step1: Create dict to hold chars and their frequencies
        ana = {}

        #Step2: iterate through one string (s)
        for c in s:
            #Step3: check if current char is already in ana, add if not
            if c not in ana:
                ana[c] = 0
            #Step4: increase count of current char
            ana[c] += 1

        #Step5: iterate through 2nd string
        for c in t:
            #Step6: check if current char is in ana, return False if not 
            if c not in ana:
                return False
            #Step7: decrease value of current char by 1
            ana[c] -= 1
            #Step8: check value is below 0, return False if it is
            if ana[c] < 0:
                return False
        #Step9: Return True if exited 2nd for loop normally
        return True