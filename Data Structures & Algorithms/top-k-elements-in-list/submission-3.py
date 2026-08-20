# Time to complete: 15 mins

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an empty hash to keep track of values and its frequency
        freq = {}

        # iterate through list and add to map and increase frequency
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # create new list
        output = []

        # add empty list inside output
        for _ in range(len(nums) + 1): # plus 1 to grab largest value        
            output.append([])

        # now turn freq into a a list where value becomes index
        for key, value in freq.items():
            output[value].append(key)
        
        # now list is sorted from smallest to largest, return k from the end
        # Create new list to grab from 
        r_list = []
        for out in output[::-1]: # ::-1 moves from end of list to front
            for num in out: # inner loop iterates over sublist, if needed
                r_list.append(num)
                if len(r_list) == k:
                    return r_list

       