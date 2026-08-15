class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Step0: Create empty hashmap for frequency
        out = {}
        
        # Step1: Iterate through list
        for num in nums:
            
            # Step2: Check if value already exists (add it if it doesn't)
            if num not in out:
                out[num] = 0

            # Step3: Increase frequency of specific value
            out[num] += 1

        # Step4: Calculate maj_element
        maj_element = len(nums) // 2

        # Step5: Find and return key of that value
        for key, value in out.items():
            if value > maj_element:
                return key