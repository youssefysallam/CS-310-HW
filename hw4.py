def maxProfit(prices):
    # variable to track max profit.
    max_profit = 0
    # loop for the prices from the second day onwards.
    for i in range(1, len(prices)):
        # If the current day's price is higher than the previous day's price, 
        # add the difference to max profit.
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
        
    return max_profit