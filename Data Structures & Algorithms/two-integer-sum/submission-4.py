class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Step0: declare hash to store seen values
        seen = {} # key = integer, value = index

        #Step1: Iterate through list, using indices
        for key, value in enumerate(nums):

            #Step2: subtract current value from target
            difference = target - value

            #Step3: check if difference in hash map, then return it's value and current key
            if difference in seen:
                return [seen[difference], key]
            
            #Step4: if not in hash, add with key being value and value being key (flip it)
            seen[value] = key