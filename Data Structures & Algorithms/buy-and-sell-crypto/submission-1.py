class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_profit = 0
        
        while end < len(prices):
            if prices[start] > prices[end]:
                start = end
                
            currentProfit = prices[end] - prices[start]
            
            if max_profit < currentProfit:
                max_profit = currentProfit
            
            # Move right to next "day"
            end += 1

        return max_profit