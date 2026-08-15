class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Choose a buy and sell date, and calculate the difference ("profit")
            # Can choose to NOT buy, making a profit of 0
        # indices represent days; if list is sorted greatest to least, then
        # no profit can be made (so choose to not buy)

        # Variables: use left @ start of list, then right is +1 
        left = 0
        right = 1
        max_profit = 0

        # While loop to prevent going past list boundaries 
        while right < len(prices):
            
            # check to see if value @ left is less than value @ right
            # assign left to right and increment right if this is true
            if prices[left] > prices[right]:
                left = right

            # profit check
            # assign curr_profit to max_profit if it's larger
            curr_profit = prices[right] - prices[left]
            if max_profit < curr_profit:
                max_profit = curr_profit
            
            # Move right to next "day"
            right += 1
        
        # return statement
        return max_profit