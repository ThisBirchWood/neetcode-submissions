class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in n:
                c = 1
                while (c+num) in n:
                    c += 1
                longest = max(longest, c)
        return longest