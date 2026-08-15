class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Problem: find the values which would store the most water
        # Need to calculate area so we need two values:
            # max height (would be the smallest of the two integers)
            # max width (max distance BETWEEN the two integers chosen)

        # 1. Variables: 
            # need two pointers (keep track of bars)
                # left set to start of index
                # right set to end (len(heights) - 1)
            # need a max_width to keep track of distance
            # max_area would be max_width * min(i, j)

        left = 0
        right = len(heights) - 1
        max_area = 0
        
        while left < right:
            # calculate area and store as max_area
            curr_area = min(heights[left], heights[right]) * (right - left)
            if max_area < curr_area:
                max_area = curr_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # return the max_area
        return max_area









