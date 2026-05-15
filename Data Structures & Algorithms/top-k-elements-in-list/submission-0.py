class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num][0] += 1
            else:
                freq[num] = [1, num]
        
        top_k = sorted(freq.values(), key=lambda x: x[0], reverse=True)
        return [top_k[i][1] for i in range(k)]


        
        