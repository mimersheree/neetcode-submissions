class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = best time to buy so far 
        # r = current day to sell 
        l, r = 0,1 
        maxP = 0

        while r < len(prices):

            # If selling today is profitable
            # calculate profit and update maximum 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:

                # Current price is lower than buy price, 
                # use it as new potential buying day 
                l = r
            
            # Move sell pointer to next day 
            r += 1
        return maxP
