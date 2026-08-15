class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Problem: Be able to find the given amount of frequent elements in an arry

        # Thoughts: Use a map to store the integer as key, then value is how often it appears?
        
        # Blank dictionary
        tracking = {}

        # Loop through list and if seen in list already increase value.
        # If not, create key: value, set value to 1
        for num in nums:
            if num not in tracking:
                tracking[num] = 0
            tracking[num] += 1
        print(tracking)
        
        # This gives us a hash map of key:value where we know have the frequency.
        # However it's unordered, so we can't find the "most frequent"
        
        # Create a empty list and append empty lists to allow for indexing
        bucket = [ [] for _ in range(len(nums) + 1)]

        print(bucket)

        # Iterate through tracking, add key as value and use value as index
        # cretes a sorted list (sorted by frequencies) with the values being the integer
        for key, value in tracking.items():
            bucket[value].append(key)
        print(bucket)

        # Create ANOTHER list to store final return list
        element =[]

        # Loop through bucket from END of list (which holds greatest frequencies)
        # Since bucket can contain multiple values at same frequency, we need to split those lists up
        for subList in bucket[::-1]:
            for num in subList:
                element.append(num)
                if len(element) == k:
                    return element
                

        
         
        
        
