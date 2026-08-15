class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create empty set (since we only need the value)
        seen_hash = set()

        # iterate through existing list
        for num in nums:
            # check if value is already in set
            if num in seen_hash:
                # return true if already found
                return True 
            # if not add it
            seen_hash.add(num)
        
        # If loop is exited naturally, then no duplicate found, return False
        return False