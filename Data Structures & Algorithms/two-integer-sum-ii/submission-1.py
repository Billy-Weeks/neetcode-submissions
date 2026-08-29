# Time to complete: 25 minis

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since array is sorted, we can test opposite ends of list at same time and decrement or increment depending if sum is > or < than target

        # two pointers:
        start = 0
        end = len(numbers) - 1

        # iterate over list
        while start < end:
            # decision if sum < target
            if numbers[start] + numbers[end] < target:
                start += 1 # increment gives a larger 1st number

            # decision if sum > target
            elif numbers[start] + numbers[end] > target:
                end -= 1 # decrement gives us smaller 2nd number

            elif numbers[start] + numbers[end] == target:
                # when target is found 
                return [start + 1, end + 1]
