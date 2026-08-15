class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Change list into a set
        set_list = set(nums)

        # Variable to keep track of longest sequence
        longest_seq = 0

        # Loop to iterate through set (not be indices, but values)
        for num in set_list:
            # Set/re-set counter for current iteration
            curr_seq = 1
            #Check if num is middle or beginning of sequeuence
            if (num - 1) not in set_list:
                
                while(num + 1) in set_list:
                    curr_seq += 1
                    num += 1
            if curr_seq > longest_seq:
                longest_seq = curr_seq
        
        return longest_seq