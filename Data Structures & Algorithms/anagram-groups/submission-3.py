class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step0: create dictionart to map tuple values
        tuple_dict = {}

        #Step1: Itearate over list of strings
        for s in strs:
            
            #Step2: Create list of size 26, filled with all 0's
            freq = [0] * 26

            #Step3: iterate over each char in current string
            for char in s:
                
                #Step4: turn char into ASCII value and normalize to map to dictionary of 26 alpha chars
                index = ord(char) - ord('a')

                #Step5: increase freq at specific index
                freq[index] += 1

            #Step6: Turn entire list into tuple to be used as key in dict
            key = tuple(freq)

            #Step7: Update dict at key (creating position if not already there)
            if key not in tuple_dict:
                tuple_dict[key] = []
            tuple_dict[key].append(s)

        #Step8: Return ONLY values of dict, converted to a list 
        return list(tuple_dict.values())

        