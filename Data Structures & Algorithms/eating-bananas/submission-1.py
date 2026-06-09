class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/k)

            if hours_taken > h:
                l = k + 1
            else:
                r = k - 1
                min_k = min(k, min_k)

        return min_k
            
            


        