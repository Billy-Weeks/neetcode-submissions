# Time to complete: 15 mins

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # If we use a set, we move all duplicates, that won't work. Plus lose index
        # Iterate through nums2, turn into dict with key = num, value = index
        nums2_hash = {}
        output = [] # return list

        for index, value in enumerate(nums2):
            if value not in nums2_hash:
                nums2_hash[value] = index
        
        # now map nums1 values to index
        for num in nums1:
            print(nums2_hash[num])
            output.append(nums2_hash[num])
        
        # return output
        return output