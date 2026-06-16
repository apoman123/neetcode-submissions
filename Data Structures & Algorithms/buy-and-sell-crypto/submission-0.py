class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        tail = len(prices)
        for j in range(tail):
            for idx in range(j+1, tail):
                if prices[idx] - prices[j] > max_profit:
                    max_profit = prices[idx] - prices[j]

        return max_profit

            