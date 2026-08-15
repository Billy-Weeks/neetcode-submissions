class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Problem: Check if a value appearss more than once

        # Step1: Create an empty set to store values in
            # Set allows for unique keys only (cannot add a value already there)
            # Set also has O(1) lookup/search
        seen = set()

        # Step2: Iterate over list
        for num in nums:
            # Step2.5: Check if element is in seen already. If it is, return True
                # Else, add to seen
            if num in seen:
                return True
            seen.add(num)
        # Step3: If for loop is exited without returning, then no duplicate exist
        return False


