class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Maximum profit when holding a stock
        hold = float('-inf')

        # Maximum profit when we sell a stock today
        sold = float('-inf')

        # Maximum profit when resting and free to buy
        rest = 0

        for price in prices:

            # Save yesterday's states before updating
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # We can continue holding or buy from yesterday's rest
            hold = max(prev_hold, prev_rest - price)

            # We can sell only if we were holding yesterday
            sold = prev_hold + price

            # We can continue resting or enter rest after cooldown
            rest = max(prev_rest, prev_sold)

        # Maximum profit when not holding a stock
        return max(sold, rest)