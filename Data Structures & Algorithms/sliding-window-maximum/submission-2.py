import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = {}
        heap = []
        res = []

        l = 0
        for r in range(len(nums)):
            n = nums[r]
            window[n] = 1 + window.get(n, 0)
            heapq.heappush(heap, n * -1)

            if r - l + 1 >= k:
                while window[heap[0] * -1] <= 0:
                    heapq.heappop(heap)
                res.append(heap[0] * -1)

                window[nums[l]] -= 1
                l += 1

        return res


