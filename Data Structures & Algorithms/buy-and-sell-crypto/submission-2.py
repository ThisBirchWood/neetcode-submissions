class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) <= 1:
            return 0

        l = 0
        r = 1

        while r < len(prices):
            l_num = prices[l]
            r_num = prices[r]
            profit = max(profit, r_num - l_num)

            if l_num >= r_num:
                l = r
            r += 1

        return profit