class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**4
        max_profit = 0
        for current in prices:
            if current < min_price:
                min_price = current
            elif current - min_price > max_profit:
                max_profit = current - min_price
        return max_profit
