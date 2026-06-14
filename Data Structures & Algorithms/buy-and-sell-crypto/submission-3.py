class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_ = float("inf")

        for i in range(len(prices)):
            price = prices[i]
            min_ = min(min_, price)
            res = max(res, price - min_)

        return res
            

