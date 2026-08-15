class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Thought: could I just loop through the list and keep a count, but that doesn't rearrange list in place

        # Step0: create pointer variable to keep track of current non-val length
        k = 0
        # Step1: Iterate over nums
        for index in range(len(nums)):
            # Step1: Compare to val
            if nums[index] == val:
                # Step2: "remove" value, keep k where it is
                nums[index] = "*"
            else:
                # Step3: swap to move non-val to front of list
                nums[k], nums[index] = nums[index], nums[k]
                # Step4: increment k
                k += 1
        # Step5: Return k
        return k