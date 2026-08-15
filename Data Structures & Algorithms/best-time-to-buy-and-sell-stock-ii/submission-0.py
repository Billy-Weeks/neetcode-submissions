class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Each integer represents cost of a stock
        # Goal is to calculate max profit using buy/sell
        # Can buy/sell any number of times per day, 
        # must only own 1 stock at a time

        # brute force? just check each to see if the price is greater?
        # initialize profit variable
        max_profit = 0

        # iterate through list, compare prices
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                max_profit += (prices[index] - prices[index - 1])
        
        return max_profit
            
       