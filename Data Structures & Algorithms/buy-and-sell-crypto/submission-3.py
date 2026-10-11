class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for profit in prices:
            min_price = min(profit, min_price)
            max_profit = max(max_profit, profit - min_price)
        return max_profit

        