class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # problem, sort in place, 0 -> 2 (have multiple of each num possible)
        # can we use a dict, then bucket sort? but then that'll take O(n) space
        # Create an empty hash, with 3 keys: 0, 1, 2. Then iterate once to count
        # number of each key, incrementing the value. THEN, use those counts to
        # overwrite original nums in order/in place

        # counting hash
        temp_dict = {"0": 0, "1": 0, "2": 0}
        
        #iterate to count
        for num in nums:
            if num == 0:
                temp_dict["0"] += 1
            elif num == 1:
                temp_dict["1"] += 1
            elif num == 2:
                temp_dict["2"] += 1
        print(temp_dict) # test print

        index = 0 # keeps track of where we're overwriting
        # transfer 0's to beginning of list
        while temp_dict["0"] > 0:
            nums[index] = 0
            temp_dict["0"] -= 1
            index += 1
        print(temp_dict)

        # add 1's next
        while temp_dict["1"] > 0:
            nums[index] = 1
            temp_dict["1"] -= 1
            index += 1
        
        # finally 2's
        while temp_dict["2"] > 0:
            nums[index] = 2
            temp_dict["2"] -= 1
            index += 1
        print(nums)

