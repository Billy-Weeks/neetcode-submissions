class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ''' Two pointers needed, one for comparison, the other
            too keep track of where the "clean" values are kept
            Then loop through list/array comparing to val swapping
            when nums[i] != val. 
        '''
        ## create a "clean index"/k
        k = 0

        ## loop through array to compare
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k