class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set up pointers(left and right)
        left = 0
        right = 1 # start after left, this one moves the most
        maxProfit = 0
        pricesLength = len(prices)

        # loop till right is at the end of the list
        while right < pricesLength:
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]

                # check if currProfit is greater than maxProfit
                if currProfit > maxProfit:
                    maxProfit = currProfit
            else: # so prices[left] > prices[right], don't buy here! lose money
                left = right
            right += 1
        
        return maxProfit