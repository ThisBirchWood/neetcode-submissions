class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2

            if k == 0:
                break

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/k)

            if hours_taken > h:
                l = k + 1
            elif hours_taken <= h:
                r = k - 1
                min_k = min(k, min_k)

        return min_k
            
            


        