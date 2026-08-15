class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Repeat the problem:
            # Take a list of integers and find the ones that repeat the most
            # Return the top k of those values
            # Ex: [1, 2, 2, 3, 3, 3], k = 2. Output: [2,3]

        # Assume k is never greater than the number of distinct elements

        # Initialize empty dictionary
        # Keys = DISTINCT integers from list
        # Values = frequency of those integers
        frequent = {}

        # Loop to populate frequency
        for num in nums:
            if num not in frequent:
                frequent[num] = 0
            frequent[num] += 1
        
        # List of list to act as bucket to "sort" frequencies
        bucket = []

        # add empty lists to bucket
        for _ in range(len(nums) + 1):
            bucket.append([])
        # Alternatively, using list comprehension: 
            # bucket = [ [] for _ in range(len(nums) + 1)]

        # iterate over frequent, pull frequency and use that as index
        # in bucket, making it's value the integer
        # This sorts dictionary without using O(n log n)
        for key, value in frequent.items():
            bucket[value].append(key)

        # Take sorted list and pull k winners from end (which is where the max lives)
        # create a final list to pull max frequeny elements
        # loop through bucket and pull sublists of values (could contain multiple values)
        # add each value to final list, then check to see if len(list) == k
        freq_elem = []

        for sublist in bucket[::-1]:
            for num in sublist:
                freq_elem.append(num)

                if len(freq_elem) == k:
                    return freq_elem



