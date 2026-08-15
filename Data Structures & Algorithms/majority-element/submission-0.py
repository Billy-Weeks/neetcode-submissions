class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ''' Iterate through list and store integer value as key
            in a dictionary and the number of occurrences as the
            value.
            Then check each value versus 'n // 2' to find majority
        '''
        empty_dict = {}

        for num in nums: ## iterate and store both index and value
            if num not in empty_dict: ## check to see if the key exists
                empty_dict[num] = 1
            else:
                empty_dict[num] += 1
        n = len(nums)
        for key, value in empty_dict.items():
            if value > n // 2:
                return key